class InstructionTree:

    def __init__(self):
        self.IL = []
        self.IIM = {}
        self.children = []
        self.parent = None
        self.sm_start = 0
        self.sm_end = -1


def printtree(curren):
    print(curren.IL)
    print(curren.IIM)
    print(curren.children)
    print(curren.sm_start, curren.sm_end)



if __name__=='__main__':
    root = InstructionTree()
    current = root

    fnum=open('resultlist.txt','r')
    m=fnum.read().split('\n')
    for n in m:
        if n!='':
            ss = n.split(':')
            f=open(ss[0],'r')
            insl=f.readlines()
            dex_pc=int(ss[1])
            ins=insl[int(ss[1])-1]
            if dex_pc in current.IIM:
                pos_in_IL = current.IIM[dex_pc]
                old_ins = current.IL[pos_in_IL]
                if old_ins != ins:
                    if current.children:
                        leave=False
                        for cld in current.children:
                            if cld.sm_start==dex_pc:
                                pos_in_IL = cld.IIM[dex_pc]
                                old_ins = cld.IL[pos_in_IL]
                                if ins==old_ins:
                                    leave=True
                                    break
                        if leave:
                            continue
                    child = InstructionTree()
                    child.parent = current
                    current.children.append(child)
                    child.sm_start = dex_pc
                    current = child
                else:
                    continue
            else:
                if current.parent is not None:
                    parent = current.parent
                    if dex_pc in parent.IIM:
                        pos_in_IL = parent.IIM[dex_pc]
                        old_ins = parent.IL[pos_in_IL]
                        if ins == old_ins:
                            current.sm_end = dex_pc
                            current = parent
                            continue
            pos_in_IL = len(current.IL)
            current.IL.append(ins)
            current.IIM[dex_pc] = pos_in_IL
    current=root
    printtree(current)
    for v in current.children:
        printtree(v)






