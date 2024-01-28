import heapq

def minimize_cable_cost(cable_lengths):
    heapq.heapify(cable_lengths)
    
    total_cost = 0
    while len(cable_lengths) > 1:
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)
        
        combined = first + second
        total_cost += combined
        
        heapq.heappush(cable_lengths, combined)
        
    return total_cost

test_cables = [
    [5, 2, 3], # 3 кабелі
    [3, 4, 7, 6, 2],  # 5 кабелів
    [12, 7, 6, 3, 9, 5, 8, 11, 4, 1] # 10 кабелів
]

for i, test_cables in enumerate(test_cables, 1):
    print(f"\nВаріант {i}")
    print("="*15)
    
    cable_lengths = test_cables[:] 
    initial_cables = len(cable_lengths)
    
    min_cost = minimize_cable_cost(cable_lengths)
    
    final_cable = cable_lengths[0] if cable_lengths else None
    final_cables = len(cable_lengths)
    
    print(f"Початкова кількість кабелів: {initial_cables}")
    print(f"Кінцева кількість кабелів: {final_cables}")  
    
    print("-"*15)
    
    print(f"Мінімальна вартість з'єднання: {min_cost}")

