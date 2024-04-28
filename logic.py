import random
import time
import tkinter as tk

Cost=1
Card_limited=5
Base_hp=20
player_hand=[]
player2_hand=[]
deployment_cost = 0
deployment_cost2 = 0


#字典部分
faction_cards = {
    1: {  # 罗德岛分支
        1: ("Amiya", 2, 1, 2),
        2: ("Kal'tsit", 3, 2, 4),
        3: ("Warfarin", 1, 1, 2),
        4: ("Mudrock", 2, 1, 4),
        5: ("Eyjafjalla", 3, 1, 4),
        6: ("Blaze", 2, 1, 5),
        7: ("W", 3, 2, 3),
        8: ("Kroos", 1, 1, 2)
    },
    2: {  # 卡西米尔分支
        1: ("Nearl", 3, 3, 1),
        2: ("Blemishine", 3, 1, 3),
        3: ("Mlynar", 4, 1, 1),
        4: ("Gravel", 1, 1, 3),
        5: ("Flametail", 2, 2, 3),
        6: ("Whislash", 1, 2, 2),
        7: ("Fartooth", 2, 3, 1),
        8: ("Platinum", 1, 1, 2)
    },
    3: {  # 大炎分支
        1: ("Ch'en", 3, 2, 4),
        2: ("Hoshiguma", 1, 1, 5),
        3: ("Swire", 1, 1, 2),
        4: ("Shu", 3, 1, 7),
        5: ("Nian", 2, 2, 3),
        6: ("Ling", 2, 1, 1),
        7: ("Chongyue", 3, 3, 3),
        8: ("Dusk", 1, 1, 2)
    },
    4: {  # Deep Sea Faction
        1: ("Skadi (Corrupt Heart)", 1, 2, 8),
        2: ("Specter", 5, 4, 6),
        3: ("Gladiia", 3, 1, 4),
        4: ("Deepcolor", 1, 1, 2),
        5: ("Andreana", 1, 1, 1),
        6: ("Seawatch", 1, 1, 2),
        7: ("Thorns", 2, 2, 3),
        8: ("Elysium", 3, 2, 5)
    },
    5: {  # Laterno Faction
        1: ("Mostima", 5, 4, 6),
        2: ("Exusiai", 2, 2, 4),
        3: ("Fiammetta", 2, 2, 6),
        4: ("Executor", 3, 3, 5),
        5: ("Sussurro", 3, 2, 6),
        6: ("Aak", 1, 1, 2),
        7: ("Beeswax", 2, 1, 3),
        8: ("Scene", 1, 2, 2)
    }
}

def loading_screen(duration):
    print("\n\n\n\n\n\nNow switch to Another player's turn.switching......\n"
          "************************************************")
    time.sleep(duration)
    print("switching completed!")

def draw_card():
    # 随机选择一个阵营
    faction = random.choice(list(faction_cards.keys()))
    # 随机选择该阵营的一张卡牌
    card_number = random.choice(list(faction_cards[faction].keys()))
    # 返回卡牌信息
    return (faction, card_number)
    drawn_card = draw_card()
    drawn_card_info = faction_cards[drawn_card[0]][drawn_card[1]]
    print(f"Drawn card: {drawn_card}")
    print(f"Card info: Name: {drawn_card_info[0]}, Cost: {drawn_card_info[1]}, Attack: {drawn_card_info[2]}, Health: {drawn_card_info[3]}")

def draw_basic_card():

    return ("Ordinary Operator", 1, 1, 1)  # 名称、费用、攻击力、生命值

##############################################################################################################
#先手玩家的函数


def player_choose_card():

    choice = input("Player A，Do you want to draw a (1) Special Card or a (2) Basic Card? Enter 1 or 2: ")
    if choice == '1':
            # 抽取特殊卡牌
            faction, card_number = draw_card()
            card_info = faction_cards[faction][card_number]
            print(f"Drawn Special Card: {card_info}")
            player_hand.append(card_info)
    elif choice == '2':
            # 抽取基础卡牌
            card_info = draw_basic_card()
            print(f"Drawn Basic Card: {card_info}")
            player_hand.append(card_info)
    else:
            print("Invalid input. Please enter 1 or 2.")
    return player_hand


def initialize_and_modify_hand():


    # 连续抽取五张卡牌，并将每张卡牌添加到玩家的手牌列表中
    for _ in range(5):
        faction, card_number = draw_card()
        card_info = faction_cards[faction][card_number]
        player_hand.append(card_info)




def remove_two_cards(player_hand):
    print("Your current hand:")
    for i, card in enumerate(player_hand):
        print(f"{i + 1}: {card}")
    choices = input("Enter the numbers of the two cards you want to remove (separated by a space): ").split()

    # 将输入转换为索引，并按照从大到小的顺序排列（这样从列表中移除时不会影响到其他索引）
    indices = sorted([int(choice) - 1 for choice in choices], reverse=True)

    # 检查索引有效性
    if all(0 <= index < len(player_hand) for index in indices):
        for index in indices:
            removed_card = player_hand.pop(index)
            print(f"Removed card: {removed_card}")
            print(f"The hand is now： {player_hand}")
    else:
        print("Invalid selection.")


def decrease_deployment_cost(amount):

    global deployment_cost  # 指明我们要修改的是全局变量
    deployment_cost -= amount  # 减少部署费用
    return deployment_cost  # 返回更新后的值


def increase_deployment_cost(amount):

    global deployment_cost  # 指明我们要修改的是全局变量
    deployment_cost += amount  # 增加部署费用
    return deployment_cost  # 返回更新后的值

 #######################################################################################################################
#后手玩家的函数

def player2_choose_card():

    choice = input("Player B，Do you want to draw a (1) Special Card or a (2) Basic Card? Enter 1 or 2: ")
    if choice == '1':
            # 抽取特殊卡牌
            faction, card_number = draw_card()
            card_info = faction_cards[faction][card_number]
            print(f"Drawn Special Card: {card_info}")
            player2_hand.append(card_info)
    elif choice == '2':
            # 抽取基础卡牌
            card_info = draw_basic_card()
            print(f"Drawn Basic Card: {card_info}")
            player2_hand.append(card_info)
    else:
            print("Invalid input. Please enter 1 or 2.")
    return player2_hand


def initialize2_and_modify_hand():


    # 连续抽取五张卡牌，并将每张卡牌添加到玩家的手牌列表中
    for _ in range(5):
        faction, card_number = draw_card()
        card_info = faction_cards[faction][card_number]
        player2_hand.append(card_info)




def remove2_two_cards(player2_hand):
    print("Your current hand:")
    for i, card in enumerate(player2_hand):
        print(f"{i + 1}: {card}")
    choices = input("Enter the numbers of the two cards you want to remove (separated by a space): ").split()

    # 将输入转换为索引，并按照从大到小的顺序排列（这样从列表中移除时不会影响到其他索引）
    indices = sorted([int(choice) - 1 for choice in choices], reverse=True)

    # 检查索引有效性
    if all(0 <= index < len(player2_hand) for index in indices):
        for index in indices:
            removed_card = player2_hand.pop(index)
            print(f"Removed card: {removed_card}")
            print(f"The hand is now： {player2_hand}")
    else:
        print("Invalid selection.")


def decrease_deployment_cost2(amount):

    global deployment_cost2  # 指明我们要修改的是全局变量
    deployment_cost2 -= amount  # 减少部署费用
    return deployment_cost2  # 返回更新后的值


def increase_deployment_cost2(amount):

    global deployment_cost2  # 指明我们要修改的是全局变量
    deployment_cost2 += amount  # 增加部署费用
    return deployment_cost2  # 返回更新后的值



#########################################################################################################################
#两个玩家的行动函数

def main_Begin_A():
    print("welcome to the game!\nYou are the first player to take a turn with the card you drew first and draw your first card."
          "\nNow draw five initial cards, you can choose three of them.")
    initialize_and_modify_hand()
    remove_two_cards(player_hand)
    player_choose_card()
    print("Your current hand: ", player_hand)
    return player_hand

def main_BEGIN_B():
    print(
        "\n\n\n\n\n\n\n*******************************************************************************\n"
        "welcome to the game!\nYou are the backgammon player to take a turn with the card you drew first and draw your first card.\nNow draw five initial cards, you can choose three of them.")
    initialize2_and_modify_hand()
    remove2_two_cards(player2_hand)
    player2_choose_card()
    print("Your current hand: ", player2_hand)
    return player2_hand

#######################################################################################################################

import tkinter as tk
from PIL import Image, ImageTk

class CardGameGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Card Battle Game")
        self.geometry("800x700")

        # 加载不同的背景图片
        self.enemy_bg_image = ImageTk.PhotoImage(Image.open("D:\\qt_p\\1024.jpg"))
        self.frontline_bg_image = ImageTk.PhotoImage(Image.open("D:\\qt_p\\1111.jpg"))
        self.ally_bg_image = ImageTk.PhotoImage(Image.open("D:\\qt_p\\1111.jpg"))
        self.button_bg_image = ImageTk.PhotoImage(Image.open("D:\\qt_p\\1111.jpg"))

        # 敌方部署行
        self.create_frame_with_background(height=200, bg_image=self.enemy_bg_image, side=tk.TOP)

        # 前线
        self.create_frame_with_background(height=200, bg_image=self.frontline_bg_image, side=tk.TOP)

        # 己方部署行
        self.create_frame_with_background(height=200, bg_image=self.ally_bg_image, side=tk.TOP)

        # 按钮区域
        self.button_frame = tk.Frame(self, height=100, bg="white")
        self.button_frame.pack(fill=tk.X, side=tk.BOTTOM)
        button_canvas = tk.Canvas(self.button_frame, height=100)
        button_canvas.pack(fill=tk.BOTH, expand=True)
        button_canvas.create_image(0, 0, image=self.button_bg_image, anchor=tk.NW)

        # 在按钮区域添加操作按钮
        self.deploy_card_button = tk.Button(button_canvas, text="Deploy Card", command=self.deploy_card)
        self.deploy_card_button.pack(side=tk.LEFT, pady=27)

        self.end_turn_button = tk.Button(button_canvas, text="End Turn", command=self.end_turn)
        self.end_turn_button.pack(side=tk.RIGHT, pady=27)

        # 你可以在这里继续添加更多按钮

    def create_frame_with_background(self, height, bg_image, side=tk.BOTTOM):
        frame = tk.Frame(self, height=height)
        frame.pack(fill=tk.X, side=side)
        canvas = tk.Canvas(frame, height=height)
        canvas.pack(fill=tk.BOTH, expand=True)
        canvas.create_image(0, 0, image=bg_image, anchor=tk.NW)
        return canvas  # 返回canvas以便可以在其上添加其他元素

    def deploy_card(self):
        # 添加放置卡牌的逻辑
        print("Deploying card...")

    def end_turn(self):
        # 添加结束回合的逻辑
        print("Ending turn...")





#######################################################################################################################
#主函数

if __name__ == '__main__':
    main_Begin_A()#1
    loading_screen(5)
    main_BEGIN_B()#2
    increase_deployment_cost(1)#1
    increase_deployment_cost2(1)#2
    loading_screen(5)
    game_gui = CardGameGUI()
    game_gui.mainloop()
