from trains.models import Train


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == goal:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))



def get_graph(qs):
    graph = {}
    for q in qs:
        graph.setdefault(q.from_city.id, set())
        graph[q.from_city_id].add(q.to_city.id)
    return graph


def get_routes(request, form):
    context = {'form': form}
    qs = Train.objects.all()
    graph = get_graph(qs)
    data = form.cleaned_data
    from_city = data['from_city']
    to_city = data['to_city']
    travel_time = data['travel_time']
    cities = data['cities']
    all_ways = list(dfs_paths(graph, from_city.id, to_city.id))
    if not len(all_ways):
        raise ValueError('Нет маршрута удовлетворяющего условиям')
    if cities:
        cities_ = [city.id for city in cities]
        right_ways = []
        for route in all_ways:
            if all(city in route for city in cities_):
                right_ways.append(route)
        if not right_ways:
            raise ValueError('Маршрут невозможен')
    else:
        right_ways = all_ways
    trains = []
    all_trains = {}
    for q in qs:
        all_trains.setdefault((q.from_city.id, q.to_city.id), [])
        all_trains[(q.from_city.id, q.to_city.id)].append(q)
    for route in right_ways:
        tmp = {}
        tmp['trains'] = []
        total_time = 0
        for i in range(len(route)-1):
            qs = all_trains[(route[i], i+1)]
            q = qs[0]
            total_time += q.travel_time
            tmp['trains'].append(q)
        tmp['total_time'] = total_time
        if total_time<=travel_time:
            trains.append(tmp)
    if not trains:
        raise ValueError('Время в пути больше заданного')
    return context

