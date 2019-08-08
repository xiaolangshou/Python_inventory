import time
from apscheduler.schedulers.blocking import BlockingScheduler

# 方法一
# def my_job():
#     print(time.time())
#
#
# sched = BlockingScheduler()
# sched.add_job(my_job, 'interval', seconds=2, args=[])
# sched.start()


# 方法二
# sched = BlockingScheduler()
# @sched.scheduled_job('interval', seconds=2)
# def my_job():
#     print(time.time())
#
#
# sched.start()


# 获得job列表
# def my_job():
#     print(time.time())
#
#
# sched = BlockingScheduler()
# job = sched.add_job(my_job, 'interval', seconds=2, id='123')
# print(sched.get_job(job_id='123'))
# print(sched.get_jobs())

# 移除作业
sched = BlockingScheduler()


def my_job():
    print(time.time())


job = sched.add_job(my_job, 'interval', seconds=2, id='123')
sched.add_job(my_job, 'interval', minutes=2, id='my_job_id')
print(sched.get_jobs())
sched.remove_job('my_job_id')
print(sched.get_jobs())
job.remove()
print(sched.get_jobs())
