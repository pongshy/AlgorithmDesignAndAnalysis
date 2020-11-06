package com.company;

import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("请输入所要输入的组数: ");
        int num = Integer.parseInt(sc.nextLine());

        while (num > 0) {
            System.out.print("请输入: ");
            String Line = sc.nextLine();
            String[] strArray = Line.split(" ");

            List<Integer> nums = new ArrayList<>();

            for (String tmp : strArray) {
                nums.add(Integer.parseInt(tmp));
            }

            List<Node> nodeList = new ArrayList<>();
            Tree tree = Tree.buildTree(nums, nodeList);

            StringBuffer buffer = new StringBuffer();
            Tree.encode(tree.getRoot(), buffer, nums.size());
            --num;
        }
        System.out.println("输入结束!");
    }
}
