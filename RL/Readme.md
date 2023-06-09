## Output

### Test Run 1
```
#######################
using Random Policy
Actions: ['A-0', 'A-1', 'A-2', 'A-3', 'A-4']
Rewards: [-1, -2,  5, -1,  3]
Selected Actions N(a): [472.0, 519.0, 501.0, 490.0, 518.0]
Max_Selected(a): A-1, Max_Reward(a):A-2
Is Max_Reward Action Used Most: False
Calculated Value Q(a): [-1.0, -2.0, 5.0, -1.0, 3.0]       
avg_reward: 1.488000187365284
#######################
using Greedy Policy
Actions: ['A-0', 'A-1', 'A-2', 'A-3', 'A-4']       
Rewards: [-1, -2,  5, -1,  3]
Selected Actions N(a): [0.0, 0.0, 0.0, 0.0, 2500.0]
Max_Selected(a): A-4, Max_Reward(a):A-2
Is Max_Reward Action Used Most: False
Calculated Value Q(a): [0.0, 0.0, 0.0, 0.0, 3.0]   
avg_reward: 3.03030303030303
#######################
using Epsilon Greedy Policy
Actions: ['A-0', 'A-1', 'A-2', 'A-3', 'A-4']       
Rewards: [-1, -2,  5, -1,  3]
Selected Actions N(a): [9.0, 4.0, 2472.0, 8.0, 7.0]
Max_Selected(a): A-2, Max_Reward(a):A-2
Is Max_Reward Action Used Most: True
Calculated Value Q(a): [-1.0, -2.0, 5.0, -1.0, 3.0]
avg_reward: 4.99049299050499
```

### Test Run 2
```
#######################
using Random Policy
Actions: ['A-0', 'A-1', 'A-2', 'A-3', 'A-4']
Rewards: [-1, -2,  5, -1,  3]
Selected Actions N(a): [529.0, 495.0, 501.0, 503.0, 472.0]
Max_Selected(a): A-0, Max_Reward(a):A-2
Is Max_Reward Action Used Most: False
Calculated Value Q(a): [-1.0, -2.0, 5.0, -1.0, 3.0]       
avg_reward: 0.3602930949590978
#######################
using Greedy Policy
Actions: ['A-0', 'A-1', 'A-2', 'A-3', 'A-4']       
Rewards: [-1, -2,  5, -1,  3]
Selected Actions N(a): [0.0, 0.0, 0.0, 0.0, 2500.0]
Max_Selected(a): A-4, Max_Reward(a):A-2
Is Max_Reward Action Used Most: False
Calculated Value Q(a): [0.0, 0.0, 0.0, 0.0, 3.0]   
avg_reward: 3.03030303030303
#######################
using Epsilon Greedy Policy
Actions: ['A-0', 'A-1', 'A-2', 'A-3', 'A-4']       
Rewards: [-1, -2,  5, -1,  3]
Selected Actions N(a): [8.0, 5.0, 2481.0, 3.0, 3.0]
Max_Selected(a): A-2, Max_Reward(a):A-2
Is Max_Reward Action Used Most: True
Calculated Value Q(a): [-1.0, -2.0, 5.0, -1.0, 3.0]
avg_reward: 5.030497990493049
```

## Test Run 3
```
#######################
using Random Policy
Actions: ['A-0', 'A-1', 'A-2', 'A-3', 'A-4']
Rewards: [-1, -2,  5, -1,  3]
Selected Actions N(a): [510.0, 495.0, 468.0, 529.0, 498.0]
Max_Selected(a): A-3, Max_Reward(a):A-2
Is Max_Reward Action Used Most: False
Calculated Value Q(a): [-1.0, -2.0, 5.0, -1.0, 3.0]
avg_reward: 1.1457318984842058
#######################
using Greedy Policy
Actions: ['A-0', 'A-1', 'A-2', 'A-3', 'A-4']
Rewards: [-1, -2,  5, -1,  3]
Selected Actions N(a): [1.0, 1.0, 2497.0, 1.0, 0.0]
Max_Selected(a): A-2, Max_Reward(a):A-2
Is Max_Reward Action Used Most: True
Calculated Value Q(a): [-1.0, -2.0, 5.0, -1.0, 0.0]
avg_reward: 5.050505050505051
#######################
using Epsilon Greedy Policy
Actions: ['A-0', 'A-1', 'A-2', 'A-3', 'A-4']
Rewards: [-1, -2,  5, -1,  3]
Selected Actions N(a): [6.0, 5.0, 2479.0, 4.0, 6.0]
Max_Selected(a): A-2, Max_Reward(a):A-2
Is Max_Reward Action Used Most: True
Calculated Value Q(a): [-1.0, -2.0, 5.0, -1.0, 3.0]
avg_reward: 4.8784050505030505
```

## Observations
1. Random Policy explores all actions more or less equally and average reward seems to be the lowest among the three policies.
2. Greedy Policy's reward is inconsistent. It sticks with the first +ve reward action it learns. After that it does not explore anymore. It is not guaranteed to learn the highest +ve reward action. If it learns the highest +ve reward action its result will be highest.
3. Epsilon-Greedy Policy's reward is more consistent. Given a low epsilon value, it keeps exploring with P(epsilon) even after discovering the +ve reward actions. Also given enough iterations, it is guaranteed to discovers the highest +ve reward action. It consistently exploit the highest +ve reward action maximum number of times.
