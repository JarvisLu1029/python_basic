# 📦 Module 9：模組 Modules

> 學習如何建立和使用自訂模組，實現程式碼的模組化

---

## 🎯 學習目標

完成本模組後，你將能夠：
- ✅ 匯入並使用標準函式庫模組
- ✅ 建立自訂模組
- ✅ 使用不同的 import 方式
- ✅ 理解 `__name__` 與 `__main__` 的用途

---

## 📂 檔案結構

| 檔案 | 內容 | 類型 |
|:---|:---|:---:|
| `9-1.py` | 📦 匯入自訂模組 | 教學 |
| `9-2.py` | 🎯 匯入特定函式 | 教學 |
| `myModule.py` | 🔧 自訂模組範例 | 模組 |

---

## 📦 匯入模組的方式

### 📋 匯入方式比較

| 方式 | 語法 | 使用方式 | 說明 |
|:---|:---|:---|:---|
| 匯入整個模組 | `import module` | `module.func()` | 需要使用模組名稱前綴 |
| 匯入並重命名 | `import module as m` | `m.func()` | 使用別名 |
| 匯入特定函式 | `from module import func` | `func()` | 直接使用函式名稱 |
| 匯入所有內容 | `from module import *` | `func()` | ⚠️ 不建議使用 |

### 📌 範例

```python
# 方式 1：匯入整個模組
import math
print(math.sqrt(16))  # 4.0

# 方式 2：使用別名
import numpy as np
arr = np.array([1, 2, 3])

# 方式 3：匯入特定函式
from math import sqrt, pi
print(sqrt(16))  # 4.0
print(pi)        # 3.141592...

# 方式 4：匯入全部（不建議）
from math import *
```

---

## 🔧 建立自訂模組

### 📋 步驟

1. 建立 `.py` 檔案（如 `myModule.py`）
2. 在檔案中定義函式和變數
3. 在其他檔案中使用 `import` 匯入

### 📌 範例：myModule.py

```python
# myModule.py

def power(base, exp):
    """計算次方"""
    return base ** exp

def split_text(text, sep=" "):
    """分割文字"""
    return text.split(sep)

# 測試模組（只在直接執行時運行）
if __name__ == "__main__":
    print(power(2, 3))  # 8
    print(split_text("Hello World"))  # ['Hello', 'World']
```

### 📌 範例：使用自訂模組

```python
# 9-1.py

# 方式 1：匯入整個模組
import myModule

result = myModule.power(2, 3)
print(result)  # 8

# 方式 2：匯入特定函式
from myModule import power, split_text

result = power(2, 3)
words = split_text("Hello World")
```

---

## 🎯 __name__ 與 __main__

### 📋 用途
- 當模組被**直接執行**時：`__name__ == "__main__"`
- 當模組被**匯入**時：`__name__ == "模組名稱"`

### 📌 範例

```python
# myModule.py

def greet(name):
    return f"Hello, {name}!"

# 這段程式碼只在直接執行 myModule.py 時運行
# 被其他檔案 import 時不會執行
if __name__ == "__main__":
    print(greet("World"))
    print("這是測試程式碼")
```

💡 **用途：** 可以在模組中加入測試程式碼，而不影響匯入的使用

---

[⬅️ 返回課程總覽](../README.md) | [上一章 Module8](../Module8/README.md)
