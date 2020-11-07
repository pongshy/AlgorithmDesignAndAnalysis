package com.pongshy.shu;

public class Dijkstra {
    // 存储i->j的最短距离
    public Integer dist[];
    // 存储前序结点
    public Integer prev[];
    // 存储边的权值信息
    public Integer c[][];
    // 矩阵规模
    public Integer n;

    // 初始化
    public Dijkstra(Integer n) {
        dist = new Integer[n];
        prev = new Integer[n];
        c = new Integer[n][n];
        this.n = n - 1;
    }


    public void Calculate(int v) {
        Boolean[] s = new Boolean[1000];

        for (int i = 1; i <= n; ++i) {
            dist[i] = c[v][i];
            s[i] = false;
            if (dist[i] == Integer.MAX_VALUE) {
                prev[i] = 0;
            } else {
                prev[i] = v;
            }
        }

        dist[v] = 0;
        s[v] = true;
        for (int i = 1; i < n; ++i) {
            int tmp = Integer.MAX_VALUE;
            int u = v;

            for (int j = 1; j <= n; ++j) {
                if ((!s[j]) && (dist[j] < tmp)) {
                    u = j;
                    tmp = dist[j];
                }
            }
            s[u] = true;
            for (int k = 1; k <= n; ++k) {
                if ((!s[k]) && (c[u][k] < Integer.MAX_VALUE)) {
                    int newdist = dist[u] + c[u][k];

                    if (newdist < dist[k]) {
                        dist[k] = newdist;
                        prev[k] = u;
                    }
                }
            }
        }

    }
}
