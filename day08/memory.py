def recurse(data):
    children, metas = data[:2]
    data = data[2:]
    scores = []
    metasum = 0

    for _ in range(children):
        total, score, data = recurse(data)
        metasum += total
        scores.append(score)

    metasum += sum(data[:metas])

    if children == 0:
        return (metasum, sum(data[:metas]), data[metas:])

    value = sum(scores[k - 1] for k in data[:metas] if 0 < k <= len(scores))
    return (metasum, value, data[metas:])

if __name__ == '__main__':
    data = [int(x) for x in input().strip().split()]
    meta, root, _data = recurse(data)
    print(meta)
    print(root)
