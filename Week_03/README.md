# 学习笔记
## 递归

将问题拆解成可重复解决的子问题。

### **模版**

包含四个部分：

1. 递归终止条件，满足该条件直接结束递归
2. 处理当前层逻辑；
3. 调用递归进入下一层；
4. 清理当前层（根据实际情况决定是否需要）。

```python
def recursion(level, param1, param2, ...): 
    # recursion terminator 
    if level > MAX_LEVEL: 
	   process_result 
	   return 

    # process logic in current level 
    process(level, data...) 

    # drill down 
    self.recursion(level + 1, p1, ...) 

    # reverse the current level status if needed
```

## 分治

递归的一种场景，相比递归模版多了`子问题拆分`和`子问题结果合并`两个步骤。

```python
def divide_conquer(problem, param1, param2, ...):
    # recursion terminator 
    if problem is None:
        print_result
        return

    # prepare data 
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)

    # conquer subproblems 
    subresult1 = self.divide_conquer(subproblems[0], p1, ...)
    subresult2 = self.divide_conquer(subproblems[1], p1, ...)
    subresult3 = self.divide_conquer(subproblems[2], p1, ...)
    …

    # process and generate the final result 
    result = process_result(subresult1, subresult2, subresult3, …)

    # revert the current level states
```

## 回溯

递归的一种场景，会在每一层递归中进行多选择，直到找到结果，通常可以用`剪枝`进行效率优化。