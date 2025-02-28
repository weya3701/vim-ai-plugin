
Python 有幾個庫可以讀取 YAML 檔案，最常用的就是 `PyYAML`。  你需要先安裝它：

```bash
pip install pyyaml
```

以下是一些使用 `PyYAML` 讀取 YAML 檔案的例子：

**方法一：  讀取整個 YAML 檔案到一個 Python 字典**

這個方法最簡單，直接將整個 YAML 檔案轉換成一個 Python 字典。

```python
import yaml

def load_yaml(filepath):
"""Loads a YAML file and returns its contents as a Python dictionary.

Args:
filepath: The path to the YAML file.

Returns:
A Python dictionary representing the YAML data, or None if an error occurs.
"""
try:
with open(filepath, 'r') as file:
yaml_data = yaml.safe_load(file)
return yaml_data
except FileNotFoundError:
print(f"Error: File not found at {filepath}")
return None
except yaml.YAMLError as e:
print(f"Error parsing YAML file: {e}")
return None

# Example usage:
filepath = 'config.yaml'  # Replace with your YAML file path
data = load_yaml(filepath)

if data:
print(data)
```

**config.yaml 檔案範例:**

```yaml
name: John Doe
age: 30
city: New York
address:
street: 123 Main St
zip: 10001
skills:
- Python
- Java
- SQL
```


**方法二：  逐行讀取 YAML 檔案 (較少使用)**

雖然比較少見，但如果你需要逐行處理 YAML 檔案，可以這樣做：

```python
import yaml

def load_yaml_line_by_line(filepath):
"""Loads a YAML file line by line (less common).

Args:
filepath: The path to the YAML file.

Returns:
A list of lines from the YAML file, or None if an error occurs.  Note that this is NOT parsed YAML data.
"""
try:
with open(filepath, 'r') as file:
lines = file.readlines()
return lines
except FileNotFoundError:
print(f"Error: File not found at {filepath}")
return None

# Example usage (this just prints the raw lines, not parsed YAML data):
filepath = 'config.yaml'
lines = load_yaml_line_by_line(filepath)
if lines:
for line in lines:
print(line.strip())
```


**注意事項:**

* 使用 `yaml.safe_load()` 比 `yaml.load()` 更安全，因為它可以防止任意程式碼執行，避免潛在的安全漏洞。  除非你非常確定你的 YAML 檔案來源安全，否則始終使用 `safe_load()`。
*  確保你的 `config.yaml` 檔案與你的 Python 檔案在同一個目錄下，或者提供完整的檔案路徑。
*  錯誤處理：程式碼包含了 `try...except` 區塊來處理檔案找不到或 YAML 解析錯誤的情況。


記得將 `'config.yaml'` 替換成你 YAML 檔案的實際路徑。  執行程式碼後，你會看到 `config.yaml` 檔案的內容被轉換成一個 Python 字典，並印在終端機上。
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1738204597.893164 108175840 init.cc:232] grpc_wait_for_shutdown_with_timeout() timed out.
