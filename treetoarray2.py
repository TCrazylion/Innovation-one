import createTree
import copy
import operator


def huanyuan(tree):
    string = ''
    node = copy.deepcopy(tree)
    cmp = operator.attrgetter('sm_start')
    parent = node.parent
    parent.children.sort(key=cmp)
    duan = len(parent.children)
    begin = 0
    start = 0
    end = 0
    for i in range(0,duan):
        end = parent.children[i].sm_start
        stop = parent.IIM[end]
        for j in range(start,stop):
            string += parent.IL[j] + '\n'
        space = ''
        for j in parent.IL[stop-1]:
            if j == ' ':
                space += ' '
            else:
                break

        string += space + 'if(a>0):\n'
        string += '    ' + parent.IL[stop] + '\n'
        string += space + 'else:\n'
        for j in parent.children[i].IL:
            string += '    ' + j + '\n'
        begin = end
        start = parent.IIM[begin] + 1
    length = len(parent.children)
    stop = len(parent.IL)
    for j in range(start, stop):
        string += parent.IL[j] + '\n'
    node = parent
    del node.children
    return string


if __name__ == '__main__':
    CT = createTree.InstructionTree()
    node,root = CT.createTree('resultlist2.txt')
    result = huanyuan(root)
    print(result)