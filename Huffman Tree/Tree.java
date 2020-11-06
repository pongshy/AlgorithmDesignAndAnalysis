package com.company;

import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

public class Tree {
    private Node root;

    public Node getRoot() {
        return root;
    }

    public void setRoot(Node node) {
        this.root = node;
    }

    // 自定义比较器，用于优先队列中
    static Comparator<Node> comparator = new Comparator<Node>() {
        @Override
        public int compare(Node o1, Node o2) {
            if (o1.getFrequence() != o2.getFrequence()) {
                return o1.getFrequence() - o2.getFrequence();
            } else {
                return o2.getSerial() - o1.getSerial();
            }
        }
    };

    // 构建二叉树
    public static Tree buildTree(List<Integer> freList, List<Node> leafs) {
        PriorityQueue<Node> priorityQueue = new PriorityQueue<Node>(comparator);

        int serial = 1;
        // 构造结点，并加入优先队列
        for (Integer tmp : freList) {
            Node node = new Node();
            node.setFrequence(tmp);
            node.setSerial(serial++);
            priorityQueue.add(node);
            leafs.add(node);
        }

        while (priorityQueue.size() != 1) {
            Node node1 = priorityQueue.poll();
            Node node2 = priorityQueue.poll();

            // 合并结点，构造子树
            Node tmpParent = new Node();
            tmpParent.setFrequence(node1.getFrequence() + node2.getFrequence());
            tmpParent.setSerial(serial++);
            // 根据频率确定两个结点位置
            if (node1.getFrequence() > node2.getFrequence()) {
                tmpParent.setLeft(node1);
                tmpParent.setRight(node2);
            } else {
                tmpParent.setLeft(node2);
                tmpParent.setRight(node1);
            }
            node1.setParent(tmpParent);
            node2.setParent(tmpParent);
            // 再次加入优先队列
            priorityQueue.add(tmpParent);
        }
        Tree tree = new Tree();
        tree.setRoot(priorityQueue.poll());
        // 返回头节点
        return tree;
    }

    // 编码并输出
    public static void encode(Node root, StringBuffer strBuffer, Integer n) {
        if (root == null) {
            return;
        }

        StringBuffer bf1 = new StringBuffer(strBuffer.toString());
        StringBuffer bf2 = new StringBuffer(strBuffer.toString());
        if (root.getLeft() != null) {
            bf1.append("0");
            encode(root.getLeft(), bf1, n);
        }
        if (root.getRight() != null) {
            bf2.append("1");
            encode(root.getRight(), bf2, n);
        }

        if (root.getSerial() >= 1 && root.getSerial() <= n) {
            System.out.println(root.getFrequence() + ": " + strBuffer.toString());
        }
    }

}
