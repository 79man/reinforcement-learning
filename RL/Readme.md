# Output

## Test Run 1 

## Four Runs Using a constant stationary reward
```
[
  {
    "policy": "Random Policy",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[-1 -2 -5 -1  6  2 -3  4  0  1]",
    "best_reward": 6,
    "best_action": "A-4",
    "training_iterations": 10000,
    "time_elapsed": 18.329581,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[1027.0, 1052.0, 1012.0, 993.0, 929.0, 977.0, 1005.0, 981.0, 1038.0, 986.0]",
      "Max_Selected(a)": "A-1",
      "Q(a)": "[-0.25, -0.5, -1.25, -0.25, 1.5, 0.5, -0.75, 1.0, 0.0, 0.25]"
    }
  },
  {
    "policy": "Greedy Policy",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[-1 -2 -5 -1  6  2 -3  4  0  1]",
    "best_reward": 6,
    "best_action": "A-4",
    "training_iterations": 10000,
    "time_elapsed": 140.17442,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[2.0, 1.0, 0.0, 1.0, 0.0, 1.0, 2.0, 9990.0, 2.0, 1.0]",
      "Max_Selected(a)": "A-7",
      "Q(a)": "[-0.1875, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5625, 1.0, 0.0, 0.0]"
    }
  },
  {
    "policy": "Epsilon Greedy Policy(0.01)",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[-1 -2 -5 -1  6  2 -3  4  0  1]",
    "best_reward": 6,
    "best_action": "A-4",
    "training_iterations": 10000,
    "time_elapsed": 92.199523,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[13.0, 14.0, 5.0, 7.0, 7893.0, 13.0, 10.0, 2033.0, 5.0, 7.0]",
      "Max_Selected(a)": "A-4",
      "Q(a)": "[-0.2499999850988388, -0.4999999925494194, -1.2451171875, -0.24993896484375, 1.5, 0.4999999701976776, -0.7499971389770508, 1.0, 0.0, 0.24993896484375]"
    }
  },
  {
    "policy": "Epsilon Greedy Policy(0.1)",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[-1 -2 -5 -1  6  2 -3  4  0  1]",
    "best_reward": 6,
    "best_action": "A-4",    
    "training_iterations": 10000,
    "time_elapsed": 136.863516,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[110.0, 116.0, 87.0, 99.0, 8898.0, 123.0, 101.0, 257.0, 112.0, 97.0]",
      "Max_Selected(a)": "A-4",
      "Q(a)": "[-0.25, -0.5, -1.25, -0.25, 1.5, 0.5, -0.75, 1.0, 0.0, 0.25]"
    }
  },
  {
    "policy": "Random Policy",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[-1 -2 -5 -1  6  2 -3  4  0  1]",
    "best_reward": 6,
    "best_action": "A-4",
    "training_iterations": 10000,
    "time_elapsed": 17.992431,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[1007.0, 989.0, 976.0, 1012.0, 1012.0, 967.0, 1002.0, 970.0, 1055.0, 1010.0]",
      "Max_Selected(a)": "A-8",
      "Q(a)": "[-0.25, -0.5, -1.25, -0.25, 1.5, 0.5, -0.75, 1.0, 0.0, 0.25]"
    }
  },
  {
    "policy": "Greedy Policy",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[-1 -2 -5 -1  6  2 -3  4  0  1]",
    "best_reward": 6,
    "best_action": "A-4",
    "training_iterations": 10000,
    "time_elapsed": 185.568,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[1.0, 1.0, 0.0, 2.0, 9994.0, 1.0, 1.0, 0.0, 0.0, 0.0]",
      "Max_Selected(a)": "A-4",
      "Q(a)": "[0.0, 0.0, 0.0, -0.1875, 1.5, 0.0, 0.0, 0.0, 0.0, 0.0]"
    }
  },
  {
    "policy": "Epsilon Greedy Policy(0.01)",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[-1 -2 -5 -1  6  2 -3  4  0  1]",
    "best_reward": 6,
    "best_action": "A-4",
    "training_iterations": 10000,
    "time_elapsed": 179.926137,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[12.0, 17.0, 10.0, 16.0, 9888.0, 7.0, 9.0, 23.0, 9.0, 9.0]",
      "Max_Selected(a)": "A-4",
      "Q(a)": "[-0.24999994039535522, -0.4999999998835847, -1.249995231628418, -0.24999999976716936, 1.5, 0.4998779296875, -0.7499885559082031, 0.9999999999999432, 0.0, 0.24999618530273438]"
    }
  },
  {
    "policy": "Epsilon Greedy Policy(0.1)",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[-1 -2 -5 -1  6  2 -3  4  0  1]",
    "best_reward": 6,
    "best_action": "A-4",
    "training_iterations": 10000,
    "time_elapsed": 137.257073,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[105.0, 101.0, 88.0, 108.0, 9011.0, 196.0, 91.0, 101.0, 108.0, 91.0]",
      "Max_Selected(a)": "A-4",
      "Q(a)": "[-0.25, -0.5, -1.25, -0.25, 1.5, 0.5, -0.75, 1.0, 0.0, 0.25]"
    }
  },
  {
    "policy": "Random Policy",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[-1 -2 -5 -1  6  2 -3  4  0  1]",
    "best_reward": 6,
    "best_action": "A-4",
    "training_iterations": 10000,
    "time_elapsed": 17.491983,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[999.0, 1040.0, 976.0, 1017.0, 1012.0, 987.0, 1005.0, 1003.0, 993.0, 968.0]",
      "Max_Selected(a)": "A-1",
      "Q(a)": "[-0.25, -0.5, -1.25, -0.25, 1.5, 0.5, -0.75, 1.0, 0.0, 0.25]"
    }
  },
  {
    "policy": "Greedy Policy",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[-1 -2 -5 -1  6  2 -3  4  0  1]",
    "best_reward": 6,
    "best_action": "A-4",
    "training_iterations": 10000,
    "time_elapsed": 197.439455,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[1.0, 0.0, 0.0, 1.0, 1.0, 9993.0, 2.0, 1.0, 1.0, 0.0]",
      "Max_Selected(a)": "A-5",
      "Q(a)": "[0.0, 0.0, 0.0, 0.0, 0.0, 0.5, -0.5625, 0.0, 0.0, 0.0]"
    }
  },
  {
    "policy": "Epsilon Greedy Policy(0.01)",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[-1 -2 -5 -1  6  2 -3  4  0  1]",
    "best_reward": 6,
    "best_action": "A-4",
    "training_iterations": 10000,
    "time_elapsed": 187.378857,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[16.0, 10.0, 9.0, 14.0, 9682.0, 225.0, 15.0, 9.0, 9.0, 11.0]",
      "Max_Selected(a)": "A-4",
      "Q(a)": "[-0.24999999976716936, -0.4999980926513672, -1.2499809265136719, -0.2499999962747097, 1.5, 0.5, -0.7499999972060323, 0.9999847412109375, 0.0, 0.2499997615814209]"
    }
  },
  {
    "policy": "Epsilon Greedy Policy(0.1)",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[-1 -2 -5 -1  6  2 -3  4  0  1]",
    "best_reward": 6,
    "best_action": "A-4",
    "training_iterations": 10000,
    "time_elapsed": 155.786133,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[119.0, 112.0, 100.0, 108.0, 8991.0, 103.0, 93.0, 177.0, 85.0, 112.0]",
      "Max_Selected(a)": "A-4",
      "Q(a)": "[-0.25, -0.5, -1.25, -0.25, 1.5, 0.5, -0.75, 1.0, 0.0, 0.25]"
    }
  },
  {
    "policy": "Random Policy",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[-1 -2 -5 -1  6  2 -3  4  0  1]",
    "best_reward": 6,
    "best_action": "A-4",
    "training_iterations": 10000,
    "time_elapsed": 17.088797,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[967.0, 977.0, 1002.0, 1074.0, 998.0, 1078.0, 941.0, 960.0, 1007.0, 996.0]",
      "Max_Selected(a)": "A-5",
      "Q(a)": "[-0.25, -0.5, -1.25, -0.25, 1.5, 0.5, -0.75, 1.0, 0.0, 0.25]"
    }
  },
  {
    "policy": "Greedy Policy",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[-1 -2 -5 -1  6  2 -3  4  0  1]",
    "best_reward": 6,
    "best_action": "A-4",
    "training_iterations": 10000,
    "time_elapsed": 194.576727,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[2.0, 1.0, 0.0, 1.0, 1.0, 1.0, 2.0, 9989.0, 2.0, 1.0]",
      "Max_Selected(a)": "A-7",
      "Q(a)": "[-0.1875, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5625, 1.0, 0.0, 0.0]"
    }
  },
  {
    "policy": "Epsilon Greedy Policy(0.01)",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[-1 -2 -5 -1  6  2 -3  4  0  1]",
    "best_reward": 6,
    "best_action": "A-4",
    "training_iterations": 10000,
    "time_elapsed": 146.670616,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[8.0, 8.0, 5.0, 6.0, 8626.0, 4.0, 11.0, 1319.0, 5.0, 8.0]",
      "Max_Selected(a)": "A-4",
      "Q(a)": "[-0.2499847412109375, -0.499969482421875, -1.2451171875, -0.249755859375, 1.5, 0.4921875, -0.7499992847442627, 1.0, 0.0, 0.2499847412109375]"
    }
  },
  {
    "policy": "Epsilon Greedy Policy(0.1)",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[-1 -2 -5 -1  6  2 -3  4  0  1]",
    "best_reward": 6,
    "best_action": "A-4",
    "training_iterations": 10000,
    "time_elapsed": 139.723185,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[130.0, 101.0, 112.0, 94.0, 8954.0, 125.0, 81.0, 193.0, 108.0, 102.0]",
      "Max_Selected(a)": "A-4",
      "Q(a)": "[-0.25, -0.5, -1.25, -0.25, 1.5, 0.5, -0.75, 1.0, 0.0, 0.25]"
    }
  }
]
```
## Learning Curve Plot
![Learning curve with constant Reward over 4Iterations](images/LearningCurve_constantReward_4Iterations.png?raw=true "Learning curve with constant Reward over 4Iterations")

## Test Run 2

## Four Runs Using a random stationary reward for each run
```
[
  {
    "policy": "Random Policy",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[  0  -9 -10 -14  -1 -11  -4  -1  -6  -7]",
    "best_reward": 0,
    "best_action": "A-0",
    "training_iterations": 10000,
    "time_elapsed": 10.141269,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[997.0, 973.0, 1014.0, 963.0, 1003.0, 1021.0, 1032.0, 1029.0, 997.0, 971.0]",
      "Max_Selected(a)": "A-6",
      "Q(a)": "[0.0, -2.25, -2.5, -3.5, -0.25, -2.75, -1.0, -0.25, -1.5, -1.75]"
    }
  },
  {
    "policy": "Greedy Policy",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[  0  -9 -10 -14  -1 -11  -4  -1  -6  -7]",
    "best_reward": 0,
    "best_action": "A-0",
    "training_iterations": 10000,
    "time_elapsed": 135.401378,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[9982.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]",
      "Max_Selected(a)": "A-0",
      "Q(a)": "[0.0, -1.6875, -1.875, -2.625, -0.1875, -2.0625, -0.75, -0.1875, -1.125, -1.3125]"
    }
  },
  {
    "policy": "Epsilon Greedy Policy(0.01)",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[  0  -9 -10 -14  -1 -11  -4  -1  -6  -7]",
    "best_reward": 0,
    "best_action": "A-0",
    "training_iterations": 10000,
    "time_elapsed": 135.291503,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[9898.0, 10.0, 9.0, 8.0, 18.0, 16.0, 12.0, 5.0, 12.0, 12.0]",
      "Max_Selected(a)": "A-0",
      "Q(a)": "[0.0, -2.2499914169311523, -2.4999618530273438, -3.499786376953125, -0.24999999998544808, -2.749999997438863, -0.9999997615814209, -0.2490234375, -1.4999996423721313, -1.7499995827674866]"
    }
  },
  {
    "policy": "Epsilon Greedy Policy(0.1)",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[  0  -9 -10 -14  -1 -11  -4  -1  -6  -7]",
    "best_reward": 0,
    "best_action": "A-0",
    "training_iterations": 10000,
    "time_elapsed": 103.99396,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[9076.0, 116.0, 91.0, 97.0, 114.0, 93.0, 116.0, 99.0, 92.0, 106.0]",
      "Max_Selected(a)": "A-0",
      "Q(a)": "[0.0, -2.25, -2.5, -3.5, -0.25, -2.75, -1.0, -0.25, -1.5, -1.75]"
    }
  },
  {
    "policy": "Random Policy",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[ -6  -5   2   1 -13 -13  -6  -6   0  -2]",
    "best_reward": 2,
    "best_action": "A-2",
    "training_iterations": 10000,
    "time_elapsed": 11.049771,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[959.0, 1020.0, 1031.0, 1027.0, 969.0, 975.0, 1035.0, 955.0, 1025.0, 1004.0]",
      "Max_Selected(a)": "A-6",
      "Q(a)": "[-1.5, -1.25, 0.5, 0.25, -3.25, -3.25, -1.5, -1.5, 0.0, -0.5]"
    }
  },
  {
    "policy": "Greedy Policy",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[ -6  -5   2   1 -13 -13  -6  -6   0  -2]",
    "best_reward": 2,
    "best_action": "A-2",
    "training_iterations": 10000,
    "time_elapsed": 137.289261,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[0.0, 2.0, 9985.0, 1.0, 2.0, 2.0, 0.0, 2.0, 4.0, 2.0]",
      "Max_Selected(a)": "A-2",
      "Q(a)": "[0.0, -0.9375, 0.5, 0.0, -2.4375, -2.4375, 0.0, -1.125, 0.0, -0.375]"
    }
  },
  {
    "policy": "Epsilon Greedy Policy(0.01)",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[ -6  -5   2   1 -13 -13  -6  -6   0  -2]",
    "best_reward": 2,
    "best_action": "A-2",
    "training_iterations": 10000,
    "time_elapsed": 128.127971,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[12.0, 12.0, 9910.0, 9.0, 8.0, 13.0, 7.0, 11.0, 9.0, 9.0]",
      "Max_Selected(a)": "A-2",
      "Q(a)": "[-1.4999996423721313, -1.2499997019767761, 0.5, 0.24999618530273438, -3.2498016357421875, -3.2499998062849045, -1.4996337890625, -1.4999985694885254, 0.0, -0.49999237060546875]"
    }
  },
  {
    "policy": "Epsilon Greedy Policy(0.1)",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[ -6  -5   2   1 -13 -13  -6  -6   0  -2]",
    "best_reward": 2,
    "best_action": "A-2",
    "training_iterations": 10000,
    "time_elapsed": 118.112,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[121.0, 92.0, 9034.0, 189.0, 84.0, 85.0, 109.0, 81.0, 109.0, 96.0]",
      "Max_Selected(a)": "A-2",
      "Q(a)": "[-1.5, -1.25, 0.5, 0.25, -3.25, -3.25, -1.5, -1.5, 0.0, -0.5]"
    }
  },
  {
    "policy": "Random Policy",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[ -9  -2   0  -9  -1  -8 -10  -6  -3   4]",
    "best_reward": 4,
    "best_action": "A-9",
    "training_iterations": 10000,
    "time_elapsed": 14.234796,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[1002.0, 952.0, 962.0, 1019.0, 944.0, 1001.0, 1061.0, 1046.0, 1007.0, 1006.0]",
      "Max_Selected(a)": "A-6",
      "Q(a)": "[-2.25, -0.5, 0.0, -2.25, -0.25, -2.0, -2.5, -1.5, -0.75, 1.0]"
    }
  },
  {
    "policy": "Greedy Policy",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[ -9  -2   0  -9  -1  -8 -10  -6  -3   4]",
    "best_reward": 4,
    "best_action": "A-9",
    "training_iterations": 10000,
    "time_elapsed": 133.058497,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 9982.0]",
      "Max_Selected(a)": "A-9",
      "Q(a)": "[-1.6875, -0.375, 0.0, -1.6875, -0.1875, -1.5, -1.875, -1.125, -0.5625, 1.0]"
    }
  },
  {
    "policy": "Epsilon Greedy Policy(0.01)",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[ -9  -2   0  -9  -1  -8 -10  -6  -3   4]",
    "best_reward": 4,
    "best_action": "A-9",
    "training_iterations": 10000,
    "time_elapsed": 129.8798,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[11.0, 12.0, 17.0, 14.0, 9.0, 14.0, 5.0, 13.0, 13.0, 9892.0]",
      "Max_Selected(a)": "A-9",
      "Q(a)": "[-2.249997854232788, -0.49999988079071045, 0.0, -2.2499999664723873, -0.24999618530273438, -1.9999999701976776, -2.490234375, -1.4999999105930328, -0.7499999552965164, 1.0]"
    }
  },
  {
    "policy": "Epsilon Greedy Policy(0.1)",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[ -9  -2   0  -9  -1  -8 -10  -6  -3   4]",
    "best_reward": 4,
    "best_action": "A-9",
    "training_iterations": 10000,
    "time_elapsed": 190.049486,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[88.0, 93.0, 122.0, 76.0, 98.0, 96.0, 108.0, 98.0, 90.0, 9131.0]",
      "Max_Selected(a)": "A-9",
      "Q(a)": "[-2.25, -0.5, 0.0, -2.25, -0.25, -2.0, -2.5, -1.5, -0.75, 1.0]"
    }
  },
  {
    "policy": "Random Policy",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[ -7 -15  -7 -12  -7  -3  -9   5  -5  -1]",
    "best_reward": 5,
    "best_action": "A-7",
    "training_iterations": 10000,
    "time_elapsed": 16.604085,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[962.0, 997.0, 1023.0, 1033.0, 976.0, 1024.0, 944.0, 989.0, 1041.0, 1011.0]",
      "Max_Selected(a)": "A-8",
      "Q(a)": "[-1.75, -3.75, -1.75, -3.0, -1.75, -0.75, -2.25, 1.25, -1.25, -0.25]"
    }
  },
  {
    "policy": "Greedy Policy",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[ -7 -15  -7 -12  -7  -3  -9   5  -5  -1]",
    "best_reward": 5,
    "best_action": "A-7",
    "training_iterations": 10000,
    "time_elapsed": 169.912963,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[2.0, 2.0, 2.0, 2.0, 2.0, 0.0, 1.0, 9985.0, 2.0, 2.0]",
      "Max_Selected(a)": "A-7",
      "Q(a)": "[-1.3125, -2.8125, -1.3125, -2.25, -1.3125, 0.0, 0.0, 1.25, -0.9375, -0.1875]"
    }
  },
  {
    "policy": "Epsilon Greedy Policy(0.01)",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[ -7 -15  -7 -12  -7  -3  -9   5  -5  -1]",
    "best_reward": 5,
    "best_action": "A-7",
    "training_iterations": 10000,
    "time_elapsed": 156.039347,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[15.0, 14.0, 7.0, 14.0, 9.0, 15.0, 12.0, 9890.0, 13.0, 11.0]",
      "Max_Selected(a)": "A-7",
      "Q(a)": "[-1.749999993480742, -3.7499999441206455, -1.74957275390625, -2.9999999552965164, -1.7499732971191406, -0.7499999972060323, -2.249999463558197, 1.25, -1.249999925494194, -0.2499997615814209]"
    }
  },
  {
    "policy": "Epsilon Greedy Policy(0.1)",
    "avm": "Exponential Recency Weighted Average",
    "rewards": "[ -7 -15  -7 -12  -7  -3  -9   5  -5  -1]",
    "best_reward": 5,
    "best_action": "A-7",
    "training_iterations": 10000,
    "time_elapsed": 169.445565,
    "summary": {
      "Actions": [
        "A-0",
        "A-1",
        "A-2",
        "A-3",
        "A-4",
        "A-5",
        "A-6",
        "A-7",
        "A-8",
        "A-9"
      ],
      "N(a)": "[122.0, 80.0, 102.0, 106.0, 104.0, 102.0, 98.0, 9056.0, 113.0, 117.0]",
      "Max_Selected(a)": "A-7",
      "Q(a)": "[-1.75, -3.75, -1.75, -3.0, -1.75, -0.75, -2.25, 1.25, -1.25, -0.25]"
    }
  }
]

```
## Learning Curve Plot
![Learning curve with random Reward over 4Iterations](images/LearningCurve_randomReward_4Iterations.png?raw=true "Learning curve with random Reward over 4Iterations")

## Learning curve constant Reward including UCB
![Learning curve constant Reward including UCB](images/LearningCurve_constantReward_includingUCB.png?raw=true "Learning curve constant Reward including UCB")

## Observations
1. Random Policy explores all actions more or less equally and average reward seems to be the lowest among the three policies.
2. Greedy Policy's reward is inconsistent. It sticks with the first +ve reward action it learns. After that it does not explore anymore. It is not guaranteed to learn the highest +ve reward action. If it learns the highest +ve reward action its result will be highest.
3. Epsilon-Greedy Policy's reward is more consistent. Given a low epsilon value, it keeps exploring with P(epsilon) even after discovering the +ve reward actions. Also given enough iterations, it is guaranteed to discovers the highest +ve reward action. It consistently exploit the highest +ve reward action maximum number of times.
4. Upper Confidence Bound Policy is basically an improvement over ϵ-greedy action selection. It forces the non-greedy actions to be tried, but not indiscriminately. Instead Actions with higher value estimates will be picked more often. Hence UCB converges fast to the ideal reward and maintains the curve better than ϵ-greedy.