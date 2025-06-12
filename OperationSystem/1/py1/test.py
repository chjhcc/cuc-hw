import heapq


class Job:
    def __init__(self, job_id, job_name, submit_time_str, service_time):
        self.job_id = job_id  # 作业编号，用于唯一标识每个作业
        self.job_name = job_name  # 作业名称，方便识别作业内容
        self.submit_time = self.convert_to_minutes(submit_time_str)  # 提交时间，转换为分钟数记录
        self.service_time = service_time  # 服务运行时间（分钟），表示作业执行所需的时间
        self.start_time = None  # 开始时间，初始化为None，后续会计算作业开始执行的时间
        self.finish_time = None  # 完成时间，初始化为None，后续会计算作业完成的时间
        self.wait_time = None  # 等待时间，初始化为None，后续会计算作业等待执行的时间
        self.turnaround_time = None  # 周转时间，初始化为None，后续会计算作业从提交到完成的总时间
        self.weighted_turnaround_time = None  # 带权周转时间，初始化为None，后续会计算周转时间与服务时间的比值

    def convert_to_minutes(self, time_str):
        """
        将时间字符串（小时:分钟格式）转换为分钟数
        :param time_str: 输入的时间字符串，格式为'小时:分钟'
        :return: 对应的分钟数
        """
        parts[0] = time_str.split(':')
        hours = int(parts)
        minutes = int(parts[1])
        return hours * 60 + minutes

    def calculate_times(self, current_time):
        """ 计算作业的开始时间、完成时间、等待时间、周转时间、带权周转时间 """
        self.start_time = current_time
        # 将当前时间设置为作业的开始时间，因为作业开始执行了
        self.finish_time = current_time + self.service_time
        # 完成时间等于开始时间加上服务运行时间
        self.wait_time = self.start_time - self.submit_time
        # 等待时间为开始时间减去提交时间
        self.turnaround_time = self.finish_time - self.submit_time
        # 周转时间为完成时间减去提交时间
        self.weighted_turnaround_time = self.turnaround_time / self.service_time
        # 带权周转时间为周转时间除以服务运行时间


def fcfs(jobs):
    """ 先来先服务调度算法 """
    jobs.sort(key=lambda job: job.submit_time)  # 按提交时间排序，使得先提交的作业排在前面
    current_time = 0
    for job in jobs:
        if current_time < job.submit_time:
            current_time = job.submit_time  # 等待作业提交，如果当前时间小于作业提交时间，就将当前时间更新为作业提交时间
        job.calculate_times(current_time)
        current_time = job.finish_time


def sjf(jobs):
    """ 短作业优先调度算法 """
    jobs.sort(key=lambda job: job.submit_time)  # 按提交时间排序，先处理先提交的作业
    ready_queue = []
    current_time = 0
    idx = 0

    while idx < len(jobs) or ready_queue:
        # 将所有已经提交的作业加入到就绪队列
        while idx < len(jobs) and jobs[idx].submit_time <= current_time:
            heapq.heappush(ready_queue, (jobs[idx].service_time, jobs[idx]))
            # 将作业按照服务时间（小顶堆）加入就绪队列，服务时间短的作业优先
            idx += 1

        if ready_queue:
            # 选择服务时间最短的作业
            _, job = heapq.heappop(ready_queue)
            job.calculate_times(current_time)
            current_time = job.finish_time
        else:
            current_time += 1  # 如果没有作业，就等1分钟，时间推进1分钟


def hrrn(jobs):
    """ 最高响应比优先调度算法 """
    jobs.sort(key=lambda job: job.submit_time)  # 按提交时间排序，先处理先提交的作业
    ready_queue = []
    current_time = 0
    idx = 0

    while idx < len(jobs) or ready_queue:
        # 将所有已经提交的作业加入到就绪队列
        while idx < len(jobs) and jobs[idx].submit_time <= current_time:
            heapq.heappush(ready_queue, (jobs[idx].submit_time, jobs[idx]))
            # 将作业按照提交时间（小顶堆）加入就绪队列
            idx += 1

        if ready_queue:
            # 计算响应比并选择响应比最高的作业
            best_job = None
            best_ratio = -float('inf')
            for _, job in ready_queue:
                waiting_time = current_time - job.submit_time
                response_ratio = (waiting_time + job.service_time) / job.service_time
                if response_ratio > best_ratio:
                    best_ratio = response_ratio
                    best_job = job
            best_job.calculate_times(current_time)
            ready_queue = [entry for entry in ready_queue if entry[1]!= best_job]  # 移除已调度作业
            current_time = best_job.finish_time
        else:
            current_time += 1  # 如果没有作业，就等1分钟，时间推进1分钟


def print_job_info(jobs):
    """ 打印作业调度信息 """
    print(f"{'作业编号':<8}{'作业名称':<8}{'提交时间':<10}{'服务时间':<10}{'开始时间':<10}{'完成时间':<10}{'等待时间':<10}{'周转时间':<10}{'带权周转时间':<10}")
    for job in jobs:
        submit_time_str = f"{job.submit_time // 60:02}:{job.submit_time % 60:02}"
        print(f"{job.job_id:<8}{job.job_name:<8}{submit_time_str:<10}{job.service_time:<10}{job.start_time:<10}{job.finish_time:<10}{job.wait_time:<10}{job.turnaround_time:<10}{job.weighted_turnaround_time:<10.2f}")


def print_statistics(jobs):
    """ 打印统计信息 """
    total_turnaround_time = sum(job.turnaround_time for job in jobs)
    total_weighted_turnaround_time = sum(job.weighted_turnaround_time for job in jobs)
    avg_turnaround_time = total_turnaround_time / len(jobs)
    avg_weighted_turnaround_time = total_weighted_turnaround_time / len(jobs)

    print(f"\n平均周转时间: {avg_turnaround_time:.2f}")
    print(f"平均带权周转时间: {avg_weighted_turnaround_time:.2f}")


def main():
    # 输入作业数据
    jobs_data = [
        (1, "JA", "2:40", 20),
        (2, "JB", "2:50", 30),
        (3, "JC", "2:55", 10),
        (4, "JD", "3:00", 24),
        (5, "JE", "3:05", 6)
    ]
    # 创建作业对象
    jobs = [Job(job_id, job_name, submit_time_str, service_time) for job_id, job_name, submit_time_str, service_time in jobs_data]
    # 选择调度方法
    print("请选择调度方法:")
    print("1. 先来先服务 (FCFS)")
    print("2. 短作业优先 (SJF)")
    print("3. 最高响应比优先 (HRRN)")
    choice = input("请输入选择的数字（1/2/3）: ").strip()
    # 根据用户选择的调度算法进行调度
    if choice == '1':
        print("\n先来先服务 (FCFS) 调度:")
        fcfs(jobs)
    elif choice == '2':
        print("\n短作业优先 (SJF) 调度:")
        sjf(jobs)
    elif choice == '3':
        print("\n最高响应比优先 (HRRN) 调度:")
        hrrn(jobs)
    else:
        print("无效的选择，请重新启动程序并选择有效的调度方法。")
        return
    # 打印作业调度信息和统计信息
    print_job_info(jobs)
    print_statistics(jobs)


if __name__ == "__main__":
    main()