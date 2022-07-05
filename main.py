import time
import random

import pyautogui

def Rand():
	return random.random() * 1.5

def move_to_pic(pic_path):
	location_ = pyautogui.locateOnScreen(pic_path)
	if location_:
		print(f'find {pic_path} success')
		x, y = pyautogui.center(location_)
		if x and y:
			pyautogui.moveTo(x, y)
			return True

def find_pic(pic_path):
	location_ = pyautogui.locateOnScreen(pic_path)
	if location_:
		return location_
	else:
		return None


def game_left_click(local):
	pyautogui.mouseDown(local, button='left')
	time.sleep(1 + Rand())
	pyautogui.mouseUp(local, button='left')

def game_right_click(local):
	pyautogui.mouseDown(local, button='right')
	time.sleep(1 + Rand())
	pyautogui.mouseUp(local, button='right')

def wait_jieshouduiju_click():
	i = 1
	while True:
		if i > 60 * 20:
			break
		print(f'等待接受对局中... 已经等待{i}次')
		home_jieshouduiju_location = find_pic('pic/home_jie_shou_dui_ju.png')
		if home_jieshouduiju_location:
			pyautogui.click(home_jieshouduiju_location)
			time.sleep(9 + Rand())
			break
		else:
			time.sleep(3 + Rand())
		i = i + 1

def match_game():
	time.sleep(2 + Rand())
	wait_jieshouduiju_click()

def into_game():
	home_zaiwanyici_location = find_pic('pic/home_zai_wan_yi_ci.png')
	if home_zaiwanyici_location:
		pyautogui.click(home_zaiwanyici_location)
		time.sleep(5 + Rand())

	home_xunzhaoduiju_location = find_pic('pic/home_xun_zhao_dui_ju.png')
	if home_xunzhaoduiju_location:
		pyautogui.click(home_xunzhaoduiju_location)
		time.sleep(5 + Rand())
		wait_jieshouduiju_click()

def expect_piece():
	location = pyautogui.locateOnScreen('pic/piece/huanjinglong.png')
	if location:
		return location


	# location = pyautogui.locateOnScreen('pic/piece/xuezhe.png')
	# if location:
	# 	return location

	# location = pyautogui.locateOnScreen('pic/piece/xxxx.png')
	# if location:
	# 	return location
	
	return None

def play_game():
	find_piece = expect_piece()

	if find_piece != None:
		game_left_click(find_piece)
		print('寻找棋子成功 点击')
	else:
		location_haikesi = pyautogui.locateOnScreen('pic/game_fuwen.png')
		if location_haikesi:
			print('点击符文')
			game_left_click(location_haikesi)

		location_zhuangbei = pyautogui.locateOnScreen('pic/game_quanbunazou.png')
		if location_zhuangbei:
			print('点击全部拿走')
			game_left_click(location_zhuangbei)

		print('寻找图片失败 开D')
		location_d = pyautogui.locateOnScreen('pic/game_d.png')
		if location_d:
			print('开D')
			game_left_click(location_d)

		#time.sleep(3)
		#pyautogui.keyUp('d')

		time.sleep(2 + Rand())


def exit_game():
	game_exit_location = find_pic('pic/game_exit.png')
	if game_exit_location:
		print('游戏结束，点击退出游戏')
		game_left_click(game_exit_location)



def game_state():
	game_tag_location = find_pic('pic/game_setting.png')

	find_location = None

	if game_tag_location:
		find_location = game_tag_location


	if find_location:
		tmp = find_pic('pic/game_map.png')
		game_right_click(tmp)
		print('====当前位于：游戏内页面====')
		return 1

	home_tag_location = find_pic('pic/home_18_yun_ding.png')
	if home_tag_location:
		game_right_click(home_tag_location)
		print('====当前位于：客户端页面====')
		return 3

	home_tag_location = find_pic('pic/home_red.png')
	if home_tag_location:
		game_right_click(home_tag_location)
		print('====当前位于：客户端页面====')
		return 3

	home_match_location = find_pic('pic/home_match.png')
	if home_match_location:
		game_right_click(home_match_location)
		print('====当前位于：匹配队列中====')
		return 4

	return - 1


if __name__ == '__main__':

	# Ezio_csm
	print('七秒后脚本将正式启动，请阅读以下说明：')
	print('启动后请保证客户端界面无遮挡')
	print('请先将游戏界面切换到云顶匹配模式寻找对局界面')
	print('请保持游戏在1080p屏幕下的默认分辨率，即客户端1280*720，游戏内1920*1080')
	print('如无法正常使用请尝试以管理员身份运行')
	print('如依然无法正常使用请尝试替换pic目录下的相关图片')
	print('该脚本适用于国服云顶V12.11版本，失效后请联系作者')

	time.sleep(7)
	print('\n脚本已启动...\n')
	#
	# print('按下')
	# pyautogui.press('d')
	# pyautogui.keyUp('d')

	while True:
		try:
			state = game_state()
			if state == 1:
				play_game()
				exit_game()
			elif state == 3:
				into_game()
			elif state == 4:
				match_game()
			else:
				print('====   未找到定位图片   ====')
			time.sleep(3 + Rand())
		except Exception as e:
			print('异常' + str(e))
