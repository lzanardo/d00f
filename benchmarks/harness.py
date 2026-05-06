from time import perf_counter

from oxdsi_cet.dsl import parse_query
from oxdsi_cet.engine import CETEngine
from oxdsi_cet.graph_model import CETGraph, EventEdge, EventVertex


def synthetic_graph(n=2000):
    from datetime import datetime, timedelta

    g = CETGraph()
    t0 = datetime.utcnow()
    for i in range(n):
        typ = ["A", "B", "C"][i % 3]
        g.add_vertex(EventVertex(str(i), "acct1", typ, t0 + timedelta(seconds=i), {"v": i}))
        if i > 0:
            g.add_edge(EventEdge(str(i - 1), str(i), "acct1", t0, t0 + timedelta(seconds=n)))
    return g


if __name__ == "__main__":
    g = synthetic_graph()
    q = parse_query("bench", ["A", "B", "C"], 600, 60)
    for mode in ["m-cet", "t-cet", "h-cet"]:
        t = perf_counter()
        out = CETEngine(mode).execute(g, q)
        print(mode, len(out), perf_counter() - t)
