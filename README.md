<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>技术博客</title>
    <style>
        body {
            background-color: #f0f0f0; /* 备用背景色 */
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }

        body::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: url('./book.jpg') center/cover no-repeat;
            opacity: 0.1; /* 让背景图透明 */
            z-index: -1;
        }

       

        /* 让 h2 居中 */
        h2 {
            font-size: 24px;
            color: black;
            text-align: center;
        }

        /* 让卡片区域居中 */
        .container {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 20px;
            padding: 20px;
        }

        /* 卡片样式 */
        .card {
            width: 180px;
            height: 100px;
            background: white;
            border-radius: 10px;
            box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
            font-weight: bold;
            text-decoration: none;
            color: black;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        /* 悬浮效果 */
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);
            background: linear-gradient(135deg, #6e8efb, #a777e3);
            color: white;
        }
    </style>
</head>

<body>

<!-- 博客时钟 -->
<div class="clock" id="clock"></div>

<h2>前端技术</h2>
<div class="container">
    <a href="前端html.html" target="_blank" class="card">HTML</a>
    <a href="CSS.html" target="_blank" class="card">CSS</a>
    <a href="VUE安装.html" class="card">VUE</a>
</div>

<h2>JAVA技术</h2>
<div class="container">
    <a href="Java基础.html" target="_blank" class="card">Java 基础</a>
    <a href="Spring.html" target="_blank" class="card">Spring</a>
    <a href="MyBatis.html" class="card">MyBatis</a>
</div>

<h2>Python技术</h2>
<div class="container">
    <a href="Python基础.html" target="_blank" class="card">Python 基础</a>
    <a href="数据分析.html" target="_blank" class="card">数据分析</a>
    <a href="机器学习.html" class="card">机器学习</a>
</div>

<h2>大数据技术</h2>
<div class="container">
    <a href="Hadoop.html" target="_blank" class="card">Hadoop</a>
    <a href="Spark.html" target="_blank" class="card">Spark</a>
    <a href="Flink.html" class="card">Flink</a>
</div>



</body>
</html>
