class BankersAlgorithm:
    def __init__(self, resources, max_demand, allocation):
        self.resources = resources  # 系统可用资源
        self.max_demand = max_demand  # 每个进程的最大需求量
        self.allocation = allocation  # 每个进程已分配的资源
        self.need = [[self.max_demand[i][j] - self.allocation[i][j] for j in range(len(resources))] for i in range(len(max_demand))] # 每个进程还需要的资源
        self.process_count = len(max_demand) # 进程数量
        self.resource_count = len(resources) # 资源种类数量

    def is_safe(self): # 判断当前系统是否处于安全状态
        work = self.resources[:] # 可用资源的副本
        finish = [False] * self.process_count # 每个进程是否已完成
        safe_sequence = [] # 安全序列

        while len(safe_sequence) < self.process_count: # 循环直到找到安全序列
            allocated = False # 是否有进程可以分配资源
            for i in range(self.process_count): # 遍历每个进程
                if not finish[i] and all(self.need[i][j] <= work[j] for j in range(self.resource_count)): # 进程可以分配资源
                    work = [work[j] + self.allocation[i][j] for j in range(self.resource_count)] # 释放资源
                    finish[i] = True # 标记进程已完成
                    safe_sequence.append(i) # 添加到安全序列
                    allocated = True # 标记已分配资源
                    break
            if not allocated: # 没有进程可以分配资源
                return False, [] # 返回不安全状态和空安全序列

        return True, safe_sequence # 返回安全状态和安全序列

    def request_resources(self, process_id, request): # 请求资源
        if any(request[j] > self.need[process_id][j] for j in range(self.resource_count)): 
            return False, "错误: 请求资源超出进程的最大需求量。"
        if any(request[j] > self.resources[j] for j in range(self.resource_count)): 
            return False, "错误: 当前没有足够的资源可分配。"

        # 假设分配资源
        self.resources = [self.resources[j] - request[j] for j in range(self.resource_count)] # 减少可用资源
        self.allocation[process_id] = [self.allocation[process_id][j] + request[j] for j in range(self.resource_count)] # 增加已分配资源
        self.need[process_id] = [self.need[process_id][j] - request[j] for j in range(self.resource_count)] # 减少还需要的资源

        safe, sequence = self.is_safe() # 判断分配后是否安全
        if not safe:
            # 回滚操作
            self.resources = [self.resources[j] + request[j] for j in range(self.resource_count)] 
            self.allocation[process_id] = [self.allocation[process_id][j] - request[j] for j in range(self.resource_count)]
            self.need[process_id] = [self.need[process_id][j] + request[j] for j in range(self.resource_count)]
            return False, "系统将进入不安全状态。"

        return True, sequence 


def main():
    resources = [10, 5, 7]  # 示例系统可用资源 A, B, C
    max_demand = [ # 示例进程的最大需求量
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3],
    ]
    allocation = [ # 示例进程已分配的资源
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2],
    ]

    ba = BankersAlgorithm(resources, max_demand, allocation) # 创建银行家算法实例

    safe, sequence = ba.is_safe() # 判断当前系统是否处于安全状态
    if safe:
        print(f"系统处于安全状态。安全序列为: {sequence}")
    else:
        print("系统处于不安全状态。")

    process_id = int(input("请输入请求资源的进程号: "))
    request = list(map(int, input("请输入请求资源数量（以空格分隔，例如 A B C）: ").split()))

    success, message = ba.request_resources(process_id, request)
    if success:
        print(f"请求已批准。新的安全序列为: {message}")
    else:
        print(f"请求被拒绝: {message}")


if __name__ == "__main__":
    main()