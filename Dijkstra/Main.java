package com.pongshy.shu;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	// write your code here
        Scanner sc = new Scanner(System.in);
        Integer index = 1;
        while (true) {
            System.out.print("请输入矩阵阶数: ");
            Integer n = Integer.parseInt(sc.nextLine());
            System.out.println("请输入各顶点之间路径长: ");

            Dijkstra dijkstra = new Dijkstra(n + 1);
            for (int i = 1; i <= n; ++i) {
                String[] strs = sc.nextLine().split(" ");
                for (int j = 1; j <= n; ++j) {
                    Integer tmp = Integer.parseInt(strs[j - 1]);
                    if (tmp < 0) {
                        tmp = Integer.MAX_VALUE;
                    }
                    dijkstra.c[i][j] = tmp;
                }
            }
            System.out.print("请输入需要输出的距离的两个顶点(用空格隔开): ");
            String[] vertex = sc.nextLine().split(" ");
            Integer start = Integer.parseInt(vertex[0]);
            Integer end = Integer.parseInt(vertex[1]);
            dijkstra.Calculate(start);

            // 输出
            System.out.println("Case " + index++);
            System.out.println("The least distance from " + start + "->" + end + " is " + dijkstra.dist[end]);
            List<Integer> out = new ArrayList<>();

            Integer pathStart = end;
            while (pathStart != start) {
                out.add(0, pathStart);
                pathStart = dijkstra.prev[pathStart];
            }
            out.add(0, start);

            StringBuffer strOut = new StringBuffer();
            strOut.append(out.get(0));
            for (int i = 1; i < out.size(); ++i) {
                strOut.append("->");
                strOut.append(out.get(i));
            }

            System.out.println("The path is " + strOut.toString());
            System.out.println();
        }
    }
}
