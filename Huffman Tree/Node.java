package com.company;

public class Node implements Comparable<Node> {
    private int frequence = 0;
    private Node parent;
    private Node left;
    private Node right;
    private Integer serial;

    private Integer test;

    public Integer getSerial() {
        return serial;
    }

    public void setSerial(Integer serial) {
        this.serial = serial;
    }

    public Integer getTest() {
        return test;
    }

    public void setTest(Integer test) {
        this.test = test;
    }

    @Override
    public int compareTo(Node o) {
        return this.frequence - o.frequence;
    }

    public Boolean isLeaf() {
        return this.left == null && this.right == null;
    }

    public Boolean isRoot() {
        return parent == null;
    }

    public Boolean isLeftChild() {
        return parent != null && this == parent.left;
    }

    public int getFrequence() {
        return frequence;
    }

    public void setFrequence(int frequence) {
        this.frequence = frequence;
    }

    public Node getParent() {
        return parent;
    }

    public void setParent(Node parent) {
        this.parent = parent;
    }

    public Node getLeft() {
        return left;
    }

    public void setLeft(Node left) {
        this.left = left;
    }

    public Node getRight() {
        return right;
    }

    public void setRight(Node right) {
        this.right = right;
    }
}
