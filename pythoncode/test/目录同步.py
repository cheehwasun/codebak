import os
import stat
from itertools import *

BUFFSIZE = 4 * 1024
DEFAULT_IGNORES = [
    'RCS', 'CVS', 'tags', '.git', '.hg', '.bzr', '_darcs', '__pycache__']

# l_only r_only 存放只有一侧存在的entry
# common_fc common_dc common_func 分别是文件，目录，和类型不同的特殊
# 三个common是个[(,)]tuple元素的list tuple0左边 tuple1右边


class my_cmpdir():
    def __init__(self, dira, dirb, ignorn=None, hide=None):
        self.left = dira
        self.rihgt = dirb
        if hide == None:
            self.hide = [os.curdir, os.pardir]
        else:
            self.hide = hide
        if ignorn == None:
            self.ignorn = DEFAULT_IGNORES
        else:
            self.ignorn = ignorn

    def mkdic(self, dir):
        return {x.name: x for x in os.scandir(dir)}

    # l_dic r_dic存放的是{path:DirEntry}
    def phase_mklist(self):
        self.l_dic = self.mkdic(self.left)
        self.r_dic = self.mkdic(self.rihgt)

    # l_only r_only存放的是DirEntry common是path chain方便递归时链接
    def phase_sep(self):
        self.l_only = chain(map(self.l_dic.__getitem__, filterfalse(
            self.r_dic.__contains__, self.l_dic)))
        self.r_only = chain(map(self.r_dic.__getitem__, filterfalse(
            self.l_dic.__contains__, self.r_dic)))
        self.common = filter(self.r_dic.__contains__, self.l_dic)

    # 处理相同的列表 分离出文件和文件夹，
    # 以及同名但是不同类型的（一个文件，一个文件夹）
    def phase_common(self):
        self.common_files = []
        self.common_dirs = []
        for each in self.common:
            ax = self.l_dic[each]
            bx = self.r_dic[each]
            a_type = stat.S_IFMT(ax.stat().st_mode)
            b_type = stat.S_IFMT(bx.stat().st_mode)
            # 文件类型不同
            if a_type != b_type:
                self.l_only = chain(self.l_only, [ax])
                self.r_only = chain(self.r_only, [bx])
            elif ax.is_dir():
                self.common_dirs.append((ax, bx))
            elif ax.is_file():
                self.common_files.append((ax, bx))
            # else:
            #     self.common_funs.append((ax, bx))
        # chain方便递归时链接 存放的是[(l-DirEntry,r-DirEntry)]
        self.common_fc = chain(self.common_files)
        # self.common_dc = chain(self.common_dirs)

    # 将子目录的对象加入subdirs数组
    def phase_subdir(self):
        # 扫描目录并进行分离
        self.phase_mklist()
        self.phase_sep()
        self.phase_common()
        self.subdirs = []
        for each in self.common_dirs:
            lp = each[0].path
            rp = each[1].path
            self.subdirs.append(my_cmpdir(lp, rp, self.ignorn, self.hide))

    # 递归调用遍历所有的相同目录，并将目录写入subdirs_chain中
    def phase_subdir_closure(self):
        self.phase_subdir()
        for each in self.subdirs:
            each.phase_subdir_closure()
            self.common_fc = chain(self.common_fc, each.common_fc)
            # self.common_dc = chain(self.common_dc, each.common_dc)
            self.l_only = chain(self.l_only, each.l_only)
            self.r_only = chain(self.r_only, each.r_only)

    # 同步文件 l_tree r_tree存放DirEntry  common_res存放(不同,相同,其他)Entry
    def sync(self):
        self.phase_subdir_closure()
        self.common_res = cmpfile(self.common_fc)

        # 下面的完整的遍历出文件列表
        # self.l_tree = scan(self.l_only)
        # self.r_tree = scan(self.r_only)

# 处理只有单边存在的文件


def scan(chain):
    l = []
    for each in chain:
        if each.is_file():
            l.append(each)
        if each.is_dir():
            l.extend(_tree(each))
    return l

# 遍历文件夹entry 返回文件entry


def _tree(entry):
    dirs = [entry]
    files = []
    while True:
        try:
            d = dirs.pop()
        except:
            break
        for each in os.scandir(d.path):
            if each.is_dir():
                dirs.append(each)
            if each.is_file():
                files.append(each)
    return files

# 比较文件加入对应的list。res[0]:不同 res[1]:相同 res[2]:异常


def cmpfile(common_fc, shallow=True):
    res = ([], [], [])
    for each in common_fc:
        res[_cmp(each[0], each[1], shallow)].append(each)
    return res

# 参数a,b对应左右两边的DirEntry


def do_cmp(a, b, shallow):
    if a.stat().st_size != b.stat().st_size:
        return False
    if a.stat().st_mtime != b.stat().st_mtime:
        return False
    if shallow:
        return True
    else:
        return _deepcmp(a.path, b.path)


def _cmp(a, b, shallow, do_cmp=do_cmp):
    try:
        return do_cmp(a, b, shallow)
    except OSError:
        return 2

# 深度比较文件


def _deepcmp(f1, f2):
    buff = BUFFSIZE
    with open(f1, 'rb') as of1, open(f2, 'rb') as of2:
        while True:
            b1 = of1.read(buff)
            b2 = of2.read(buff)
            if b1 != b2:
                return False
            if not b1:
                return True
