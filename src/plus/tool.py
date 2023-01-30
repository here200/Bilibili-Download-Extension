# 打印容器的数据
def print_container_elements(container):
    for el in container:
        print(el)
    print()


# 捕获异常的执行函数
def execute_function(func):
    try:
        func()
    except Exception:
        pass
