import java.util.*;
import java.io.*;

public class Main {
    static Map<Integer, Integer> id = new HashMap<Integer, Integer>();

    static int getId(int spot) {
        Integer v = id.get(spot);
        if (v == null) {
            v = id.size();
            id.put(spot, v);
        }
        return v;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<String> lines = new ArrayList<String>();
        String s;
        while ((s = br.readLine()) != null) {
            s = s.trim();
            if (s.length() > 0) lines.add(s);
        }
        int n = Integer.parseInt(lines.get(0));
        String[] q = lines.get(n + 1).split("\\s+");
        int cur = Integer.parseInt(q[0]);
        int dest = Integer.parseInt(q[1]);

        // each entry: {tree, lowerSpotId, upperSpotId or -1}
        List<int[]> es = new ArrayList<int[]>();
        int tree = 0;
        for (int i = 1; i <= n; i++) {
            String ln = lines.get(i);
            if (ln.equalsIgnoreCase("break")) {
                tree++;
                continue;
            }
            String[] tk = ln.split("\\s+");
            int lo = getId(Integer.parseInt(tk[0]));
            if (tk.length == 1) es.add(new int[]{tree, lo, -1});
            for (int j = 1; j < tk.length; j++) {
                int hi = getId(Integer.parseInt(tk[j]));
                es.add(new int[]{tree, lo, hi});
            }
        }
        int T = tree + 1;

        if (cur == dest) {
            System.out.println(0);
            return;
        }
        Integer cs = id.get(cur), ds = id.get(dest);
        if (cs == null || ds == null) {
            System.out.println(-1);
            return;
        }
        int V = id.size();

        List<List<Integer>> up = new ArrayList<List<Integer>>();
        List<List<Integer>> down = new ArrayList<List<Integer>>();
        for (int i = 0; i < T * V; i++) {
            up.add(new ArrayList<Integer>());
            down.add(new ArrayList<Integer>());
        }
        boolean[][] in = new boolean[T][V];
        for (int[] e : es) {
            in[e[0]][e[1]] = true;
            if (e[2] < 0) continue;
            in[e[0]][e[2]] = true;
            up.get(e[0] * V + e[1]).add(e[2]);
            down.get(e[0] * V + e[2]).add(e[1]);
        }

        final int INF = Integer.MAX_VALUE;
        int[] dist = new int[T * V];
        Arrays.fill(dist, INF);
        PriorityQueue<int[]> pq = new PriorityQueue<int[]>(11, new Comparator<int[]>() {
            public int compare(int[] x, int[] y) {
                return Integer.compare(x[0], y[0]);
            }
        });
        for (int t = 0; t < T; t++) {
            if (in[t][cs]) {
                dist[t * V + cs] = 0;
                pq.add(new int[]{0, t, cs});
            }
        }
        while (!pq.isEmpty()) {
            int[] c = pq.poll();
            int d = c[0], t = c[1], v = c[2];
            if (d > dist[t * V + v]) continue;
            for (int w : up.get(t * V + v)) {                       // climb up: cost 1
                if (d + 1 < dist[t * V + w]) {
                    dist[t * V + w] = d + 1;
                    pq.add(new int[]{d + 1, t, w});
                }
            }
            for (int w : down.get(t * V + v)) {                     // climb down: free
                if (d < dist[t * V + w]) {
                    dist[t * V + w] = d;
                    pq.add(new int[]{d, t, w});
                }
            }
            for (int t2 = 0; t2 < T; t2++) {                        // switch tree: cost 1
                if (t2 != t && in[t2][v] && d + 1 < dist[t2 * V + v]) {
                    dist[t2 * V + v] = d + 1;
                    pq.add(new int[]{d + 1, t2, v});
                }
            }
        }

        int ans = INF;
        for (int t = 0; t < T; t++) ans = Math.min(ans, dist[t * V + ds]);
        System.out.println(ans == INF ? -1 : ans);
    }
}