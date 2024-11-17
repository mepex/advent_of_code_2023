import re
import csv
from binarytree import Node


class Rule:
    """A simple example class"""
    i = 12345

    def __init__(self, d):
        result = re.match(r"(\w+){(.*)}", d)
        if result:
            self.name = result.group(1)
            c = result.group(2)
            s = c.split(',')
            self.cond = []
            self.has_approval = False
            for i in s:
                j = i.split(':')
                if len(j) > 1:
                    self.cond.append((j[0], j[1]))
                    if j[1] == 'A':
                        self.has_approval = True
                else:
                    self.cond.append((j[0], ''))
                    if j[0] == 'A':
                        self.has_approval = True

    def __str__(self):
        return self.name

    def run(self, l):
        definitions = l[1:-1].split(',')
        for item in definitions:
            exec(item)
        index = 0
        answer = None
        while re.search(r'[><=]', self.cond[index][0]):
            condition = self.cond[index][0]
            possible_answer = self.cond[index][1]
            if eval(condition):
                answer = possible_answer
                break
            else:
                index += 1

        if answer:
            return answer
        else:
            return self.cond[index][0]

    def get_approval_conditions(self):
        if not self.has_approval:
            return None
        a = []
        for c in self.cond:
            if c[1] == 'A':
                a.append(c[0])
                return a
            elif c[0] != 'A':
                a.append(f"not {c[0]}")
        return a

class Rules:
    def __init__(self):
        self.r = {}

    def add_rule(self, l):
        r = Rule(l)
        self.r[str(r)] = r

    def get_rating(l):
        definitions = l[1:-1].split(',')
        r = 0
        for item in definitions:
            t = item.split('=')
            r += int(t[1])
        return r

    def run(self, l):
        result = self.r['in'].run(l)
        while result != 'A' and result != 'R':
            result = self.r[result].run(l)
        if result == 'A':
            return Rules.get_rating(l)
        else:
            return 0

    def find_segments(self):
        for key in self.r:
            a = self.r[key].get_approval_conditions()
            if a:
                print(f"{key} : {a}")

    def make_tree(self, wf):
        cond = self.r[wf].cond
        root = Node(cond[0][0])
        n = root
        if cond[0][1] == 'A':
            root.iff = Node('A')
        if cond[0][1] == 'R':
            root.iff = Node('R')

        for c in cond[1:]:
            q = cond[c][0]
            iff = cond[c][1]
            if '<' in q or '>' in q:
                o = Node(q)

            if iff == '':
                return root
            elif iff != 'A' and iff != 'R':
                o = Node(c[0])
                n.iff = o
                root.iff = self.make_tree(cond[c][1])
            else:
                pass

    def build_root(self) -> Node:
        self.root = self.build_tree('in')
        return self.root

    def build_tree(self, wf) -> Node:
        cond = self.r[wf].cond
        root = Node(cond[0][0])
        if cond[0][1] == 'A' or cond[0][1] == 'R':
            root.left = Node(cond[0][1])
        else:
            root.left = self.build_tree(cond[0][1])
        n = root
        for c in cond[1:]:
            q = c[0]
            iff = c[1]
            if q == 'A' or q == 'R':
                n.right = Node(q)
                break
            else:
                if ">" in q or "<" in q:
                    o = Node(q)
                    n.right = o
                else:
                    n.right = self.build_tree(q)
                if iff == 'A' or iff == 'R':
                    o.left = Node(iff)
                elif iff == '':
                    return root
                else:
                    n.right = self.build_tree(iff)
            n = o

        return root


    def tree_paths(n : Node) -> list:

        if not n.left and not n.right:
            return [[n.value]]
        r = n.right
        l = n.left
        paths = []
        if n.left:
            for l in Rules.tree_paths(n.left):
                paths.append([n.value] + l)
        if n.right:
            for r in Rules.tree_paths(n.right):
                paths.append([n.value] + r)
        return paths

    def build_paths(self):
        self.paths = Rules.tree_paths(self.root)
        self.paths = [value for value in self.paths if value[-1] == 'A']
        return self.paths





    def brute_force_segments(self):
        t = 0
        for x in range(1,4001):
            print(f"x={x}")
            for m in range(1,4001):
                for a in range(1,4001):
                    for s in range(1,4001):
                        r = self.run(f"{{x={x},m={m},a={a},s={s}}}")
                        if r:
                            t += 1









    def f(self):
        return 'hello world'