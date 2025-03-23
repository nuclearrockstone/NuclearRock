# PythonDecorator

## 装饰器

### 要点

- Python中一切皆为对象，因此函数可以作为另一个函数的参数和返回值

- 装饰器的作用是在定义函数时为函数在原函数的基础上添加一种通用功能
    - 输出日志

    - 统计运行时间

    - 权限验证


- 用于装饰其他函数的函数是一个闭包，其获取一个函数作为输入，并将函数打包后输出

- 装饰器的语法是Python中的一种语法糖

### 装饰器语法

**装饰器示例**

```powershell
def decorator(func): #获取函数作为输入
    print("Def function {} using decorator".format(func.__name__))
    def wraper(*args,**kwards): #使用不定参数，使用输入原函数的输入执行原函数
        print("Wrap function {}".format(func.__name__))
        func(*args,**kwards)
    return wraper #返回函数作为输出

@decorator
def original_func(msg = "none"):
    print("Run original_func with {}".format(msg))

print("\n")
original_func("TEST RUN 1")

print("\n")
original_func("TEST RUN 2")
```

```powershell
Def function original_func using decorator


Wrap function original_func
Run original_func with TEST RUN 1


Wrap function original_func
Run original_func with TEST RUN 2
```

**装饰器的等效语法**

- 在定义函数`func`时`@decorator`等效于执行如下语句
    `func = decorator(func)`


- 若装饰器本身有参数，定义时使用`@decorator(param)`等效于
    `func = decorator(param)(func)`


```powershell
def original_func_2(msg = "none"):
    print("Run original_func_2 with {}".format(msg))

decorated_original_func_2 = decorator(original_func_2)

print("\n")
decorated_original_func_2("TEST RUN 1")

print("\n")
decorated_original_func_2("TEST RUN 2")
```

```powershell
Def function original_func_2 using decorator


Wrap function original_func_2
Run original_func_2 with TEST RUN 1


Wrap function original_func_2
Run original_func_2 with TEST RUN 2
```

**有参数的装饰器**

```powershell
def decorator_takeparam(msg="none"):
    print("Def decorator with msg {}".format(msg))
    def decorator_real(func):
        print("Def function {} using decorator".format(func.__name__))
        def wraper(*args,**kwards):
            print("Wrap with msg {}".format(msg))
            print("Wrap function {}".format(func.__name__))
            func(*args,**kwards)
        return wraper
    return decorator_real

@decorator_takeparam("TEST DEF")
def original_func_3(msg = "none"):
    print("Run original_func_2 with {}".format(msg))

print("\n")
original_func_3("TEST RUN 1")

print("\n")
original_func_3("TEST RUN 2")
```

```powershell
Def decorator with msg TEST DEF
Def function original_func_3 using decorator


Wrap with msg TEST DEF
Wrap function original_func_3
Run original_func_2 with TEST RUN 1


Wrap with msg TEST DEF
Wrap function original_func_3
Run original_func_2 with TEST RUN 2
```

