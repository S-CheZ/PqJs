# <div align="center">🚀 PqJs - PyQt Web引擎逆向工具</div>

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.7+-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

**基于PyQt Web引擎的高效JavaScript逆向解决方案**

[特性](#特性) • [演示视频](#演示视频) • [安装](#安装) • [快速开始](#快速开始) • [使用指南](#使用指南) • [示例](#示例) • [常见问题](#常见问题) • [交流群](#交流群)

</div>

## ✨ 特性

- 🎯 **环境免补** - 直接使用PyQt Web引擎执行JS代码，无需复杂的环境补全
- ⚡ **高效稳定** - 经过严格测试，支持大多数网站的反爬逆向
- 🛠️ **多版本支持** - 提供命令行和代码集成两种使用方式
- 🔧 **跨平台** - 支持Windows、Linux、macOS系统
- 📦 **开箱即用** - 提供预编译版本，无需配置复杂环境

## 📺 演示视频
想快速了解PqJs的使用方法和效果？观看演示视频：

[点击此处观看B站演示视频](https://www.bilibili.com/video/BV1LdSFBUEpt/?spm_id_from=333.1007.top_right_bar_window_history.content.click&vd_source=ced1e9febd036a116f88b9bb5e696c96)



视频内容涵盖：

📱 PqJs基本使用方法演示

🔧 命令行版本实战操作

💻 代码集成版本调用示例

⚡ 实际逆向案例效果展示

🎯 多种应用场景实战



## 🚀 安装

### 方式一：下载预编译版本（推荐）

前往 [Release页面](https://github.com/S-CheZ/PqJs/releases) 下载对应系统的可执行文件：

- **Windows**: `PqJs_windows_x64.exe`
- **Linux**: `PqJs_linux_x64` 
- **macOS**: `PqJs_macos_x64`

### 方式二：源码安装

```bash
# 克隆项目
git clone https://github.com/S-CheZ/PqJs.git
cd PqJs

# 安装依赖
pip install -r requirements.txt
```

## 🎯 快速开始

### 命令行版本

```bash
# 基本用法
PqJs.exe script.js

# 指定目标网站
PqJs.exe -url "https://target-website.com" script.js

# 查看帮助
PqJs.exe -h
```

### 代码集成版本

```python

# 基本调用

# 加密代码块
javascript_code = """
   function getSign() {
       return "your_sign_value";
   }
   console.log(getSign())
"""

result = getSign(javascript_code)
print(result)

# 指定目标网站调用
result = getSign(javascript_code, "https://target-website.com")
```

## 📖 使用指南

### 命令行参数详解

| 参数 | 简写 | 必选 | 说明 |
|------|------|------|------|
| `input_file` | - | ✅ | 要执行的JavaScript文件路径 |
| `--url` | `-u` | ❌ | 目标网站URL（可选） |
| `--help` | `-h` | ❌ | 显示帮助信息 |

### 函数接口

```python
def getSign(javascript: str, url: str = "") -> str:
    """
    执行JavaScript代码并返回结果
    
    Args:
        javascript: 要执行的JavaScript代码字符串
        url: 目标网站URL（建议先不填写，如报错再补充）
    
    Returns:
        执行结果字符串
    """
```

## 💡 示例

### 示例1：简单的签名生成

**sign.js**
```javascript
function generateSign(data) {
    // 模拟签名算法
    var timestamp = Date.now();
    var sign = md5(data + timestamp + "secret_key");
    return sign;
}

generateSign("example_data");
```

**执行命令**
```bash
PqJs.exe sign.js
```

### 示例2：复杂环境检测绕过

**bypass.js**
```javascript
(function() {
    // 复杂的浏览器环境检测
    if (window.self === window.top) {
        // 环境检测逻辑
        var fingerprint = generateFingerprint();
        return encrypt(fingerprint);
    }
    return "environment_error";
})();
```

**执行命令**
```bash
PqJs.exe -url "https://protected-site.com" bypass.js
```

## ⚠️ 注意事项

### Linux系统环境变量

在Linux系统中运行时，可能需要设置以下环境变量：

```bash
export QT_QUICK_BACKEND=software
export QMLSCENE_DEVICE=softwarecontext
export QT_X11_NO_MITSHM=1
export QT_NO_GLUT=1
```

### 使用建议

1. **优先不指定URL**：首先尝试不指定url参数执行，如遇到问题再添加目标网站URL
2. **错误排查**：如执行失败，检查JavaScript代码的兼容性
3. **性能优化**：对于复杂JS代码，建议进行适当优化以提高执行效率

## 🐛 常见问题

**Q: 执行时出现Qt相关错误怎么办？**  
A: 确保系统中已安装必要的Qt依赖库，或使用预编译版本。

**Q: JavaScript代码执行超时怎么办？**  
A: 检查JS代码中是否有死循环，或尝试简化代码逻辑。

**Q: 如何获取最新的预编译版本？**  
A: 关注GitHub Release页面获取最新版本。

## 🤝 交流群

遇到问题？想要交流学习？欢迎加入我们的技术交流群：

<div align="center">

| 微信群 | QQ群 |
|:---:|:---:|
| <img src="https://github.com/S-GGbond/PqJs/blob/main/img/wx.jpeg" width="200" alt="微信群"> | <img src="https://github.com/S-GGbond/PqJs/blob/main/img/qq.jpeg" width="200" alt="QQ群"> |

</div>

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

感谢所有为这个项目贡献代码和提出建议的开发者们！

---

<div align="center">

**如果这个项目对你有帮助，请给个⭐Star支持一下！**

</div>
