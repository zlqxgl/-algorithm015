学习笔记

本周的学习重点是哈希表、树、堆和图。

哈希在python中就是字典，常用于统计元素数量后生成的字典。在附件PPT里总结了 ，常用的字典的方法。枚举字典的键，枚举字典的值，以元组的形式枚举字典元素等。

树是二维结构中最重要的数据结构，应用较多的是二叉树，常用的二叉树的前中后序遍历和层序遍历，另外二叉搜索树的特点以及插入和删除流程，也是重点。对树而言，由于重复性高，所以经常用到递归。例如前面的斐波那契数列，本质就是递归树。

堆的概念相对抽象，将一列数据放入堆中，可以迅速返回最小值（小根堆）或者最大值（大根堆）。常见有二叉堆、斐波那契堆，二叉堆（不是二叉搜索树）的插入和删除比较特殊。插入时先插到末端，然后向上排序。删除顶端元素时，先将末端元素替换到顶端，然后重排。目前对堆的认识还不够深刻（疑问，python中对列表或者字典求最大元素，直接用MAX函数就可以，还需要用堆吗？），后续多做题吧。

图，树如有回连的地方就形成图，图基本元素包括点和边，常用DFS和BFS算法，其中必须包含vistied=set()。