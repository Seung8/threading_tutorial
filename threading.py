import threading

class Messenger(threading.Thread):
	"""
	threading library를 이용한 Python thread 구현 실습
	출처: https://creativeworks.tistory.com/entry/PYTHON-3-Tutorials-31-Threading-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%98-%EC%93%B0%EB%A0%88%EB%94%A9?category=620431 

	Thread는 관용적으로 run() 함수를 통해 실행하며
	Thread.start() 처럼 start() 함수를 통해 실행할 경우 
	자동으로 해당 Thread 클래스에서 run() 메소드를 찾아서 실행해준다.
	"""
	def run(self):
		# 10번의 순회 Loop를 만든다. 단순 loop가 목적인 경우 변수는 _로 지정한다.
		for _ in range(10):
			print(threading.currentThread().getName())

# send 스레드 생성
send = Messenger(name='Sending out messages')
# receiver 스레드 생성
receiver = Messenger(name='Receiving out messages')

send.start()
receiver.start()
