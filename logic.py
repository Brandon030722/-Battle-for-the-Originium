import random
import time
import tkinter as tk

Cost=1
Card_limited=5
Base_hp=20
player_hand=[]
player2_hand=[]
deployment_cost = 10
deployment_cost2 = 0



#字典部分
faction_cards = {
    1: {  # 罗德岛分支
        1: ("Amiya", 2, 1, 2, "D:\\qt_p\\agent\\OIP.JPG"),
        2: ("Kal'tsit", 3, 2, 4, "D:\\qt_p\\agent\\OIP.JPG"),
        3: ("Warfarin", 1, 1, 2, "D:\\qt_p\\agent\\OIP.JPG"),
        4: ("Mudrock", 2, 1, 4, "D:\\qt_p\\agent\\OIP.JPG"),
        5: ("Eyjafjalla", 3, 1, 4, "D:\\qt_p\\agent\\OIP.JPG"),
        6: ("Blaze", 2, 1, 5, "D:\\qt_p\\agent\\OIP.JPG"),
        7: ("W", 3, 2, 3, "D:\\qt_p\\agent\\OIP.JPG"),
        8: ("Kroos", 1, 1, 2, "D:\\qt_p\\agent\\OIP.JPG")
    },
    2: {  # 卡西米尔分支
        1: ("Nearl", 3, 3, 1, "D:\\qt_p\\agent\\OIP.JPG"),
        2: ("Blemishine", 3, 1, 3, "D:\\qt_p\\agent\\OIP.JPG"),
        3: ("Mlynar", 4, 1, 1, "D:\\qt_p\\agent\\OIP.JPG"),
        4: ("Gravel", 1, 1, 3, "D:\\qt_p\\agent\\OIP.JPG"),
        5: ("Flametail", 2, 2, 3, "D:\\qt_p\\agent\\OIP.JPG"),
        6: ("Whislash", 1, 2, 2, "D:\\qt_p\\agent\\OIP.JPG"),
        7: ("Fartooth", 2, 3, 1, "D:\\qt_p\\agent\\OIP.JPG"),
        8: ("Platinum", 1, 1, 2, "D:\\qt_p\\agent\\OIP.JPG")
    },
    3: {  # 大炎分支
        1: ("Ch'en", 3, 2, 4, "D:\\qt_p\\agent\\OIP.JPG"),
        2: ("Hoshiguma", 1, 1, 5, "D:\\qt_p\\agent\\OIP.JPG"),
        3: ("Swire", 1, 1, 2, "D:\\qt_p\\agent\\OIP.JPG"),
        4: ("Shu", 3, 1, 7, "D:\\qt_p\\agent\\OIP.JPG"),
        5: ("Nian", 2, 2, 3, "D:\\qt_p\\agent\\OIP.JPG"),
        6: ("Ling", 2, 1, 1, "D:\\qt_p\\agent\\OIP.JPG"),
        7: ("Chongyue", 3, 3, 3, "D:\\qt_p\\agent\\OIP.JPG"),
        8: ("Dusk", 1, 1, 2, "D:\\qt_p\\agent\\OIP.JPG")
    },
    4: {  # Deep Sea Faction
        1: ("Skadi (Corrupt Heart)", 1, 1, 3, "D:\\qt_p\\agent\\OIP.JPG"),
        2: ("Specter", 3, 3, 3, "D:\\qt_p\\agent\\OIP.JPG"),
        3: ("Gladiia", 3, 1, 4, "D:\\qt_p\\agent\\OIP.JPG"),
        4: ("Deepcolor", 1, 1, 2, "D:\\qt_p\\agent\\OIP.JPG"),
        5: ("Andreana", 1, 1, 1, "D:\\qt_p\\agent\\OIP.JPG"),
        6: ("Highmore", 1, 1, 2, "D:\\qt_p\\agent\\OIP.JPG"),
        7: ("Thorns", 2, 2, 3, "D:\\qt_p\\agent\\OIP.JPG"),
        8: ("irene", 3, 2, 5, "D:\\qt_p\\agent\\OIP.JPG")
    },
    5: {  # Laterno Faction
        1: ("Mostima", 5, 4, 6, "D:\\qt_p\\agent\\OIP.JPG"),
        2: ("Exusiai", 2, 2, 4, "D:\\qt_p\\agent\\OIP.JPG"),
        3: ("Fiammetta", 2, 2, 6, "D:\\qt_p\\agent\\OIP.JPG"),
        4: ("Executor", 3, 3, 5, "D:\\qt_p\\agent\\OIP.JPG"),
        5: ("Virtuosa", 3, 2, 6, "D:\\qt_p\\agent\\OIP.JPG"),
        6: ("Archetto", 1, 1, 2, "D:\\qt_p\\agent\\OIP.JPG"),
        7: ("Spuria", 2, 1, 3, "D:\\qt_p\\agent\\OIP.JPG"),
        8: ("insider", 1, 2, 2, "D:\\qt_p\\agent\\OIP.JPG")
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
    if deployment_cost >= amount:
        deployment_cost -= amount
        print(f"Current deployment cost after decrease: {deployment_cost}")
    else:
        print("Not enough cost available.")
    return deployment_cost  # 返回更新后的值


def increase_deployment_cost(amount):

    global deployment_cost  # 指明我们要修改的是全局变量
    deployment_cost += amount  # 增加部署费用
    print(f"Current deployment cost after increase: {deployment_cost}")
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
        self.title(" Battle for the Originium")
        self.geometry("800x700")

        # 初始化用于存储图像引用的列表
        self.card_images = []

        self.load_background_images()
        self.setup_game_areas()
        self.add_buttons()

    def load_background_images(self):
        # 加载所有背景图片
        self.enemy_bg_image = ImageTk.PhotoImage(Image.open("D:\\qt_p\\1.jpg"))
        self.frontline_bg_image = ImageTk.PhotoImage(Image.open("D:\\qt_p\\3.jpg"))
        self.ally_bg_image = ImageTk.PhotoImage(Image.open("D:\\qt_p\\2.jpg"))
        self.button_bg_image = ImageTk.PhotoImage(Image.open("D:\\qt_p\\1111.jpg"))

    def setup_game_areas(self):
        # 创建并设置所有游戏区域
        self.enemy_deployment_frame = self.create_frame_with_background(200, self.enemy_bg_image, tk.TOP)
        self.frontline_frame = self.create_frame_with_background(200, self.frontline_bg_image, tk.TOP)
        self.ally_deployment_frame = self.create_frame_with_background(200, self.ally_bg_image, tk.TOP)


    def add_buttons(self):
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

    def create_frame_with_background(self, height, bg_image, side):
        frame = tk.Frame(self, height=height)
        frame.pack(fill=tk.X, side=side)
        canvas = tk.Canvas(frame, height=height)
        canvas.pack(fill=tk.BOTH, expand=True)
        canvas.create_image(0, 0, image=bg_image, anchor=tk.NW)
        return canvas

    def deploy_card(self):
        if not player_hand:
            print("No cards to deploy.")
            return
        print("Select a card to deploy by index:")
        for index, card in enumerate(player_hand, start=1):
            print(f"{index}. {card[0]} (Cost: {card[1]}, Attack: {card[2]}, Health: {card[3]})")
        choice = int(input("Enter card number: ")) - 1
        card = player_hand[choice]
        if len(card) < 5:
            print("Card data is incomplete.")
            return
        name, cost, attack, health, img_path = card
        if deployment_cost >= cost:
            self.show_card_on_ally_deployment(img_path, name)
            decrease_deployment_cost(cost)
        else:
            print("Not enough deployment cost.")
            deploy_card(self)

    def show_card_on_ally_deployment(self, img_path, card_name):
        # 显示卡牌在己方部署行
        img = Image.open(img_path)
        img = img.resize((100, 180), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(img)
        self.card_images.append(photo_img)  # 保存图像引用
        num_cards = len(self.card_images) - 1
        self.ally_deployment_frame.create_image(10 + 110 * num_cards, 10, image=photo_img, anchor=tk.NW)
        print(f"Deployed {card_name}")

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
    game_gui = CardGameGUI()#1
    game_gui.mainloop()#1
