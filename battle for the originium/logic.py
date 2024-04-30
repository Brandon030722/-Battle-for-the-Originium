import random
import time
import tkinter as tk
import pickle



Cost=1
Card_limited=5
Base1_hp=20
Base2_hp=20
player_hand=[]
player2_hand=[]
deployment_cost = 10
deployment_cost2 = 10




#字典部分
faction_cards = {
    1: {  # 罗德岛分支
        1: ("Amiya", 2, 1, 2, "D:\\battle for the originium\\Battle for the originium\\Luodedao\\Amiya.png"),
        2: ("Kal'tsit", 3, 2, 4, "D:\\battle for the originium\\Battle for the originium\\Luodedao\\Kal'tsit.png"),
        3: ("Warfarin", 1, 1, 2, "D:\\battle for the originium\\Battle for the originium\\Luodedao\\Warfarin.png"),
        4: ("Mudrock", 2, 1, 4, "D:\\battle for the originium\\Battle for the originium\\Luodedao\\Mudrock.png"),
        5: ("Eyjafjalla", 3, 1, 4, "D:\\battle for the originium\\Battle for the originium\\Luodedao\\Eyjafjalla.png"),
        6: ("Blaze", 2, 1, 5, "D:\\battle for the originium\\Battle for the originium\\Luodedao\\Blaze.png"),
        7: ("W", 3, 2, 3, "D:\\battle for the originium\\Battle for the originium\\Luodedao\\W.png"),
        8: ("Kroos", 1, 1, 2, "D:\\battle for the originium\\Battle for the originium\\Luodedao\\Kroos.png")
    },
    2: {  # 卡西米尔分支
        1: ("Nearl", 3, 3, 1, "D:\\battle for the originium\\Battle for the originium\\Kaximier\\Nearl.png"),
        2: ("Blemishine", 3, 1, 3, "D:\\battle for the originium\\Battle for the originium\\Kaximier\\Blemishine.png"),
        3: ("Mlynar", 4, 1, 1, "D:\\battle for the originium\\Battle for the originium\\Kaximier\\Mlynar.png"),
        4: ("Gravel", 1, 1, 3, "D:\\battle for the originium\\Battle for the originium\\Kaximier\\Gravel.png"),
        5: ("Flametail", 2, 2, 3, "D:\\battle for the originium\\Battle for the originium\\Kaximier\\Flametail.png"),
        6: ("Whislash", 1, 2, 2, "D:\\battle for the originium\\Battle for the originium\\Kaximier\\Whislash.png"),
        7: ("Fartooth", 2, 3, 1, "D:\\battle for the originium\\Battle for the originium\\Kaximier\\Fartooth.png"),
        8: ("Platinum", 1, 1, 2, "D:\\battle for the originium\\Battle for the originium\\Kaximier\\Platinum.png")
    },
    3: {  # 大炎分支
        1: ("Ch'en", 3, 2, 4, "D:\\battle for the originium\\Battle for the originium\\Dayan\\chen.png"),
        2: ("Hoshiguma", 1, 1, 5, "D:\\battle for the originium\\Battle for the originium\\Dayan\\Hoshiguma.png"),
        3: ("Swire", 1, 1, 2, "D:\\battle for the originium\\Battle for the originium\\Dayan\\Swire.png"),
        4: ("Shu", 3, 1, 7, "D:\\battle for the originium\\Battle for the originium\\Dayan\\shu.png"),
        5: ("Nian", 2, 2, 3, "D:\\battle for the originium\\Battle for the originium\\Dayan\\nian.png"),
        6: ("Ling", 2, 1, 1, "D:\\battle for the originium\\Battle for the originium\\Dayan\\ling.png"),
        7: ("Chongyue", 3, 3, 3, "D:\\battle for the originium\\Battle for the originium\\Dayan\\chongyue.png"),
        8: ("Dusk", 1, 1, 2, "D:\\battle for the originium\\Battle for the originium\\Dayan\\Dusk.png")
    },
    4: {  # Deep Sea Faction
        1: ("Skadi", 1, 1, 3, "D:\\battle for the originium\\Battle for the originium\\Shenhailieren\\Skadi.png"),
        2: ("Specter", 3, 3, 3, "D:\\battle for the originium\\Battle for the originium\\Shenhailieren\\Specter.png"),
        3: ("Gladiia", 3, 1, 4, "D:\\battle for the originium\\Battle for the originium\\Shenhailieren\\Gladiia.png"),
        4: ("Deepcolor", 1, 1, 2, "D:\\battle for the originium\\Battle for the originium\\Shenhailieren\\Deepcolor.png"),
        5: ("Andreana", 1, 1, 1, "D:\\battle for the originium\\Battle for the originium\\Shenhailieren\\Andreana.png"),
        6: ("Highmore", 1, 1, 2, "D:\\battle for the originium\\Battle for the originium\\Shenhailieren\\Highmore.png"),
        7: ("Thorns", 2, 2, 3, "D:\\battle for the originium\\Battle for the originium\\Shenhailieren\\Thorns.png"),
        8: ("irene", 3, 2, 5, "D:\\battle for the originium\\Battle for the originium\\Shenhailieren\\irene.png")
    },
    5: {  # Laterno Faction
        1: ("Mostima", 5, 4, 6, "D:\\battle for the originium\\Battle for the originium\\Latelan\\Mostima.png"),
        2: ("Executor", 2, 2, 4, "D:\\battle for the originium\\Battle for the originium\\Latelan\\Executor.png"),
        3: ("Fiammetta", 2, 2, 6, "D:\\battle for the originium\\Battle for the originium\\Latelan\\Fiammetta.png"),
        4: ("Executor", 3, 3, 5, "D:\\battle for the originium\\Battle for the originium\\Latelan\\Executor.png"),
        5: ("Virtuosa", 3, 2, 6, "D:\\battle for the originium\\Battle for the originium\\Latelan\\Virtuosa.png"),
        6: ("Archetto", 1, 1, 2, "D:\\battle for the originium\\Battle for the originium\\Latelan\\Archetto.png"),
        7: ("Spuria", 2, 1, 3, "D:\\battle for the originium\\Battle for the originium\\Latelan\\Spuria.png"),
        8: ("insider", 1, 2, 2, "D:\\battle for the originium\\Battle for the originium\\Latelan\\insider.png")
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


'''
def save_game_state(self):
    print("Saving enemy deployed cards:", self.enemy_deployed_cards)  # 添加这一行来检查保存的卡牌数据
    game_state = {
        'player1_deployed_cards': self.deployed_cards,
        'player2_deployed_cards': self.enemy_deployed_cards,
        'frontline_cards': self.frontline_cards
    }
    with open('game_state.pkl', 'wb') as f:
        pickle.dump(game_state, f)
    print("Game state saved.")

def load_game_state(self):
    try:
        with open('game_state.pkl', 'rb') as f:
            game_state = pickle.load(f)
        self.deployed_cards = game_state['player1_deployed_cards']
        self.enemy_deployed_cards = game_state['player2_deployed_cards']
        self.frontline_cards = game_state['frontline_cards']
        print("Loaded enemy deployed cards:", self.enemy_deployed_cards)  # 添加这一行来检查加载的卡牌数据
        self.update_ally_deployment()
        self.update_enemy_deployment()
        self.update_frontline_deployment()
        print("Game state loaded.")
    except FileNotFoundError:
        print("No saved game state found.")
'''

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
#两个玩家的初始函数和行动函数

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

def main_action_A():
    print("\nNow it's your turn.\n")
    player_choose_card()
    print("Your current hand: ", player_hand)
    return player_hand

def main_action_B():
    print("\nNow it's your turn.\n")
    player2_choose_card()
    print("Your current hand: ", player2_hand)
    return player2_hand

#######################################################################################################################
#前端部分
import tkinter as tk
from PIL import Image, ImageTk



class CardGameGUI(tk.Tk):
    def __init__(self, player_number=1):
        super().__init__()
        self.player_number = player_number
        self.title(f"Battle for the Originium - Player {self.player_number}")
        self.geometry("800x700")

        # 根据玩家号分配手牌和部署成本
        if self.player_number == 1:
            self.current_hand = player_hand
            self.deployment_cost = deployment_cost
        else:
            self.current_hand = player2_hand
            self.deployment_cost = deployment_cost2

        # 为每个玩家初始化已部署和敌方卡牌列表
        self.deployed_cards = []
        self.enemy_deployed_cards = []
        self.frontline_cards = []
        self.card_images = []

        self.load_background_images()
        self.setup_game_areas()
        self.add_buttons()
        self.attacked_this_turn = {}  # 追踪每张卡本回合是否已经攻击


#######################################################################################################################
#存储和加载游戏状态
    def save_game_state(self):
        game_state = {
            'deployed_cards': self.deployed_cards,
            'frontline_cards': self.frontline_cards
        }
        with open('game_state.pkl', 'wb') as f:
            pickle.dump(game_state, f)
        print("Game state saved.")

    def load_game_state(self):
        try:
            with open('game_state.pkl', 'rb') as f:
                game_state = pickle.load(f)
                self.deployed_cards = game_state['deployed_cards']
                self.frontline_cards = game_state['frontline_cards']
                self.update_ally_deployment()
                self.update_frontline_deployment()
                print("Game state loaded.")
        except FileNotFoundError:
            print("No saved game state found.")
            # If no game state is found, do not load anything (start new)


    def load_background_images(self):
        # 加载所有背景图片
        self.enemy_bg_image = ImageTk.PhotoImage(Image.open("D:\\qt_p\\1.jpg"))
        self.frontline_bg_image = ImageTk.PhotoImage(Image.open("D:\\qt_p\\3.jpg"))
        self.ally_bg_image = ImageTk.PhotoImage(Image.open("D:\\qt_p\\2.jpg"))
        self.button_bg_image = ImageTk.PhotoImage(Image.open("D:\\qt_p\\1111.jpg"))
#######################################################################################################################
#设置画布与按钮
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

        # 新添加的移动到前线的按钮
        self.move_to_frontline_button = tk.Button(button_canvas, text="Move to Frontline",
                                                  command=self.move_card_to_frontline)
        self.move_to_frontline_button.pack(side=tk.LEFT, padx=10, pady=27)

        self.attack_button = tk.Button(button_canvas, text="Attack", command=self.attack_card)
        self.attack_button.pack(side=tk.LEFT, padx=10, pady=27)

    # 你可以在这里继续添加更多按钮


#######################################################################################################################
#游戏开始阶段


    def start_new_game(self):
        # 重置游戏状态，确保从空白开始
        self.deployed_cards = []
        self.frontline_cards = []
        self.update_ally_deployment()
        self.update_frontline_deployment()
        print("New game started.")

    def create_frame_with_background(self, height, bg_image, side):
        frame = tk.Frame(self, height=height)
        frame.pack(fill=tk.X, side=side)
        canvas = tk.Canvas(frame, height=height)
        canvas.pack(fill=tk.BOTH, expand=True)
        canvas.create_image(0, 0, image=bg_image, anchor=tk.NW)
        return canvas

    def deploy_card(self):
        if not self.current_hand:
            print("No cards to deploy.")
            return
        print("Select a card to deploy by index:")
        for index, card in enumerate(self.current_hand, start=1):
            print(f"{index}. {card[0]} (Cost: {card[1]}, Attack: {card[2]}, Health: {card[3]})")
        choice = int(input("Enter card number: ")) - 1
        if choice < 0 or choice >= len(self.current_hand):
            print("Invalid choice.")
            return
        card = self.current_hand.pop(choice)
        if len(card) < 5:
            print("Card data is incomplete.")
            return
        name, cost, attack, health, img_path = card
        if self.deployment_cost >= cost:
            self.show_card_on_deployment(img_path, name, cost, attack, health, self.player_number == 2)  # 添加是否敌方的参数
            self.deployment_cost -= cost
        else:
            print("Not enough deployment cost.")

    def display_card(self, card_data, canvas, index):
        # 从路径加载图片
        img = Image.open(card_data['img'])
        img = img.resize((100, 180), Image.Resampling.LANCZOS)  # 调整图片大小
        photo_img = ImageTk.PhotoImage(img)
        self.card_images.append(photo_img)  # 保存图像引用以防垃圾回收
        # 计算图像放置位置
        x_position = 10 + 110 * index
        y_position = 10
        # 在画布上创建图像
        image_id = canvas.create_image(x_position, y_position, image=photo_img, anchor=tk.NW)
        # 更新卡牌数据以包含新的 image_id
        card_data['image_id'] = image_id

    def show_card_on_deployment(self, img_path, card_name, cost, attack, health, is_enemy):
        img = Image.open(img_path)
        img = img.resize((100, 180), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(img)
        self.card_images.append(photo_img)  # 保存图像引用
        deployment_frame = self.enemy_deployment_frame if is_enemy else self.ally_deployment_frame
        deployed_cards = self.enemy_deployed_cards if is_enemy else self.deployed_cards
        num_cards = len(deployed_cards)
        x_position = 10 + 110 * num_cards
        y_position = 10
        image_id = deployment_frame.create_image(x_position, y_position, image=photo_img, anchor=tk.NW)
        card_data = {
            'img': img_path,
            'image_id': image_id,
            'name': card_name,
            'cost': cost,
            'attack': attack,
            'health': health
        }
        deployed_cards.append(card_data)

    def show_card_on_ally_deployment(self, img_path, card_name, cost, attack, health):
        # 显示卡牌在己方部署行
        img = Image.open(img_path)
        img = img.resize((100, 180), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(img)
        self.card_images.append(photo_img)  # 保存图像引用
        num_cards = len(self.deployed_cards)
        image_id = self.ally_deployment_frame.create_image(10 + 110 * num_cards, 10, image=photo_img, anchor=tk.NW)
        self.deployed_cards.append({
            'img': img_path,
            'image_id': image_id,
            'name': card_name,
            'cost': cost,
            'attack': attack,
            'health': health
        })
        print(f"Deployed {card_name}")

    def show_card_on_enemy_deployment(self, img_path, card_name, cost, attack, health):
            img = Image.open(img_path)
            img = img.resize((100, 180), Image.Resampling.LANCZOS)
            photo_img = ImageTk.PhotoImage(img)
            self.card_images.append(photo_img)
            num_cards = len(self.enemy_deployed_cards)
            image_id = self.enemy_deployment_frame.create_image(10 + 110 * num_cards, 10, image=photo_img, anchor=tk.NW)
            self.enemy_deployed_cards.append({
                'img': img_path,
                'image_id': image_id,
                'name': card_name,
                'cost': cost,
                'attack': attack,
                'health': health
            })
            print(f"Deployed {card_name} on enemy area")

    def end_turn(self):
        self.save_game_state()  # 保存游戏状态
        print("Ending turn and saving game state. Switching to next player.")
        self.destroy()  # 关闭当前窗口

    def remove_card_from_ally(self, card_index):
        # 此函数负责从己方部署位中移除选中的卡牌
        if 0 <= card_index < len(self.deployed_cards):
            card_data = self.deployed_cards.pop(card_index)
            # 从画布上删除卡牌的图像
            self.ally_deployment_frame.delete(card_data['image_id'])
            return card_data
        else:
            print("Invalid card index")
            return None

    def deploy_card_to_frontline(self, card_data):
        img_path = card_data['img']
        img = Image.open(img_path)
        img = img.resize((100, 180), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(img)
        self.card_images.append(photo_img)  # 保存图像引用防止被回收
        image_id = self.frontline_frame.create_image(10 + 110 * len(self.frontline_cards), 10, image=photo_img,
                                                     anchor=tk.NW)
        card_data['image_id'] = image_id
        card_data['player_number'] = self.player_number  # 添加此行
        self.frontline_cards.append(card_data)




#######################################################################################################################
#更新展示的代码
    def update_ally_deployment(self):
        self.ally_deployment_frame.delete("all")
        self.ally_deployment_frame.create_image(0, 0, image=self.ally_bg_image, anchor=tk.NW)
        for idx, card_data in enumerate(self.deployed_cards):
            self.display_card(card_data, self.ally_deployment_frame, idx)

    def update_frontline_deployment(self):
        # 同理，更新前线显示
        existing_images = {card_data['image_id']: card_data for card_data in self.frontline_cards}
        self.frontline_frame.delete("all")  # 重新绘制背景
        self.frontline_frame.create_image(0, 0, image=self.frontline_bg_image, anchor=tk.NW)

        updated_cards = []
        for idx, card_data in enumerate(self.frontline_cards):
            img_path = card_data['img']
            img = Image.open(img_path)
            img = img.resize((100, 180), Image.Resampling.LANCZOS)
            photo_img = ImageTk.PhotoImage(img)
            self.card_images.append(photo_img)
            if card_data['image_id'] in existing_images:
                self.frontline_frame.delete(card_data['image_id'])
            image_id = self.frontline_frame.create_image(10 + 110 * idx, 10, image=photo_img, anchor=tk.NW)
            card_data['image_id'] = image_id
            updated_cards.append(card_data)

        self.frontline_cards = updated_cards

    def update_enemy_deployment(self):
        self.enemy_deployment_frame.delete("all")  # 先清除画布
        self.enemy_deployment_frame.create_image(0, 0, image=self.enemy_bg_image, anchor=tk.NW)  # 重置背景
        # 重新绘制每一张卡牌
        for idx, card_data in enumerate(self.enemy_deployed_cards):
            self.display_card(card_data, self.enemy_deployment_frame, idx)
        print("Enemy cards updated.")


######################################################################################################################
#移动至前线
    def move_card_to_frontline(self):
        cards_to_move = self.deployed_cards if self.player_number == 1 else self.enemy_deployed_cards

        if not cards_to_move:
            print("No cards to move.")
            return

        print("Select a card to move to the frontline by index:")
        for index, card_data in enumerate(cards_to_move, start=1):
            print(
                f"{index}. Name: {card_data['name']} (Cost: {card_data['cost']}, Attack: {card_data['attack']}, Health: {card_data['health']})")

        choice = int(input("Enter card number: ")) - 1
        if 0 <= choice < len(cards_to_move):
            card_data = cards_to_move.pop(choice)
            if self.player_number == 2 and any(c.get('player_number', 1) == 1 for c in self.frontline_cards):
                print("Cannot move to frontline; enemy cards present.")
                cards_to_move.insert(choice, card_data)  # 如果不能移动，把卡牌放回原位
            else:
                self.deploy_card_to_frontline(card_data)
                self.update_ally_deployment()  # 更新己方部署区域
                self.update_enemy_deployment()  # 更新敌方部署区域
                self.update_frontline_deployment()  # 更新前线显示
        else:
            print("Invalid card index")


#######################################################################################################################
#战斗部分

    def initiate_attack(self):
        # 显示可攻击的卡牌
        print("Select a card to attack with:")
        deployed_cards = self.deployed_cards if self.player_number == 1 else self.enemy_deployed_cards
        frontline_cards = self.frontline_cards
        for index, card in enumerate(deployed_cards + frontline_cards, start=1):
            print(f"{index}. {card['name']} (Attack: {card['attack']}, Health: {card['health']})")

        choice = int(input("Enter card number: ")) - 1
        if 0 <= choice < len(deployed_cards + frontline_cards):
            attacking_card = (deployed_cards + frontline_cards)[choice]
            self.select_target(attacking_card)
        else:
            print("Invalid card index")

    def select_target(self, attacking_card):
        # 确定目标集合
        target_cards = self.enemy_deployed_cards if attacking_card in self.deployed_cards else self.deployed_cards
        print("Select a target card to attack:")
        for index, card in enumerate(target_cards, start=1):
            print(f"{index}. {card['name']} (Health: {card['health']})")

        choice = int(input("Enter target card number: ")) - 1
        if 0 <= choice < len(target_cards):
            target_card = target_cards[choice]
            self.execute_attack(attacking_card, target_card)
        else:
            print("Invalid target card index")

    def execute_attack(self, attacking_card, target_card):
        # 执行攻击，扣除生命值
        target_card['health'] -= attacking_card['attack']
        print(
            f"Attacked {target_card['name']} with {attacking_card['name']}, remaining health: {target_card['health']}")
        # 检查目标卡牌生命值
        if target_card['health'] <= 0:
            self.remove_card(target_card)

    def remove_card(self, card_to_remove):
        # 从显示和内部数据中移除卡牌
        frame_to_update = self.enemy_deployment_frame if card_to_remove in self.enemy_deployed_cards else self.ally_deployment_frame
        frame_to_update.delete(card_to_remove['image_id'])
        card_list = self.enemy_deployed_cards if card_to_remove in self.enemy_deployed_cards else self.deployed_cards
        card_list.remove(card_to_remove)
        print(f"{card_to_remove['name']} has been removed from the field.")

    def attack_card(self):
        # 分别获取当前玩家和对手的部署区和前线卡牌
        current_player_cards = self.deployed_cards if self.player_number == 1 else self.enemy_deployed_cards
        frontline_cards = [card for card in self.frontline_cards if card['player_number'] == self.player_number]
        attackable_cards = current_player_cards + frontline_cards

        if not attackable_cards:
            print("No cards available to attack.")
            return

        print("Select your card to attack with:")
        for idx, card_data in enumerate(attackable_cards):
            print(f"{idx + 1}. {card_data['name']} (Attack: {card_data['attack']}, Health: {card_data['health']})")

        card_index = int(input("Enter card number: ")) - 1
        if card_index < 0 or card_index >= len(attackable_cards):
            print("Invalid choice.")
            return

        attacking_card = attackable_cards[card_index]
        # 确定攻击目标：如果在部署区，攻击前线；如果在前线，攻击对方部署区
        if attacking_card in current_player_cards:
            possible_targets = self.frontline_cards
        else:
            possible_targets = self.enemy_deployed_cards if self.player_number == 1 else self.deployed_cards

        if not possible_targets:
            print("No targets available.")
            return

        print("Select a target to attack:")
        for idx, card_data in enumerate(possible_targets):
            print(f"{idx + 1}. {card_data['name']} (Health: {card_data['health']})")

        target_index = int(input("Enter target number: ")) - 1
        if target_index < 0 or target_index >= len(possible_targets):
            print("Invalid target.")
            return

        target_card = possible_targets[target_index]
        # 执行攻击
        target_card['health'] -= attacking_card['attack']
        print(f"{attacking_card['name']} attacked {target_card['name']} for {attacking_card['attack']} damage.")
        if target_card['health'] <= 0:
            possible_targets.remove(target_card)  # 目标卡牌被销毁
            print(f"{target_card['name']} has been destroyed!")
        else:
            print(f"{target_card['name']} now has {target_card['health']} health.")

        self.update_ally_deployment()  # 更新己方部署区域显示
        self.update_enemy_deployment()  # 更新敌方部署区域显示
        self.update_frontline_deployment()  # 更新前线显示


#######################################################################################################################
#主函数

if __name__ == '__main__':


    # 玩家1的游戏开始
    main_Begin_A()
    increase_deployment_cost(1)  # 1
    game_gui = CardGameGUI(player_number=1)
    game_gui.mainloop()

    # 玩家2的游戏开始
    main_BEGIN_B()
    increase_deployment_cost2(1)  # 2
    game_gui = CardGameGUI(player_number=2)
    game_gui.load_game_state()
    game_gui.mainloop()

    while Base1_hp > 0 and Base2_hp > 0:
     main_action_A()
     game_gui = CardGameGUI(player_number=1)
     game_gui.load_game_state()
     game_gui.mainloop()

     if Base1_hp <= 0 or Base2_hp <= 0:
         break

     main_action_B()
     game_gui = CardGameGUI(player_number=2)
     game_gui.load_game_state()
     game_gui.mainloop()
     if Base1_hp <= 0 or Base2_hp <= 0:
        break

     print("Game Over")




while Base1_hp > 0 and Base2_hp > 0:
        # 玩家1的回合
        game_gui_player1 = CardGameGUI(player_number=1)
        game_gui_player1.load_game_state()
        main_action_A()  # 玩家1进行操作
        game_gui_player1.save_game_state()  # 保存游戏状态
        game_gui_player1.mainloop()  # 处理界面事件，等待回合结束

        # 检查游戏是否已结束
        if Base1_hp <= 0 or Base2_hp <= 0:
            break

        # 玩家2的回合
        game_gui_player2 = CardGameGUI(player_number=2)
        game_gui_player2.load_game_state()
        main_action_B()  # 玩家2进行操作
        game_gui_player2.save_game_state()  # 保存游戏状态
        game_gui_player2.mainloop()  # 处理界面事件，等待回合结束

        # 检查游戏是否已结束
        if Base1_hp <= 0 or Base2_hp <= 0:
            break

        print("Game Over")
