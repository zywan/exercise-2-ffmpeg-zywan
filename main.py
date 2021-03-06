import subprocess
import threading
from queue import Queue

class MyThread(threading.Thread):
	def __init__(self, queue):
		threading.Thread.__init__(self)
		self.queue = queue

	def run(self):
		while not self.queue.empty():
			print('there are ', threading.activeCount(), 'threads running')
			task = self.queue.get()
			mission = subprocess.call(task)
			self.queue.task_done
			print("mission", task, 'finished')


def main():
	task_queue = Queue()
	for i in range(3):
		name = ['480p_'+str(i)+'.mp4', '720p_'+str(i)+'.mp4']
		task = ['ffmpeg', '-i', 'video.mp4',
		  		'-r', '30', '-s', 'hd480', '-b:v', '1024k', '-loglevel', 'quiet', name[0],
				'-r', '30', '-s', 'hd720', '-b:v', '2048k', '-loglevel', 'quiet', name[1]]
		task_queue.put(task)
	thread_num = 2
	for i in range(thread_num):
		thread_convert = MyThread(task_queue)
		thread_convert.start()

	task_queue.join()
	print('all done')


if __name__ == '__main__':
	main()