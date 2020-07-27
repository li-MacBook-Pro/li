from random import randint
import pygal
class Die():
    """表示一个骰子的类"""
    def __init__(self, num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides
    def roll(self):
        """"返回一个位于1和骰子面数之间的随机值"""
        return randint(1, self.num_sides)
'''掷一个骰子'''
'''
die=Die()
# 掷几次骰子，并将结果存储在一个列表中￼ 
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)
# 分析结果
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
# 对结果进行可视化￼ 
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3','4', '5','6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
'''
'''同时掷两个骰子'''
'''
# 创建两个D6骰子￼ 
die_1 = Die()
die_2 = Die()
# 掷骰子多次，并将结果存储到一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll()+die_2.roll()
    results.append(result)
# 分析结果￼ 
frequencies = []
max_result = die_1.num_sides+die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
# 可视化结果￼ 
hist = pygal.Bar()
hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6+D6', frequencies)
hist.render_to_file('dice_visual.svg')
'''
'''同时掷两个面数不同的骰子'''
'''
# 创建一个D6和一个D10￼ 
die_1 = Die()
die_2 = Die(10)
# 掷骰子多次，并将结果存储在一个列表中￼ 
results = []
for roll_num in range(50000):
    result = die_1.roll()+die_2.roll()
    results.append(result)
# 分析结果￼ --snip--￼
frequencies = []
max_result = die_1.num_sides+die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
# 可视化结果
hist = pygal.Bar()
hist.title = "Results of rolling a D6 and a D10 50,000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12','13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6+D10',frequencies)
hist.render_to_file('dice_visual.svg')
'''