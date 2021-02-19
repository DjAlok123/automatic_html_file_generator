import os

def main():

	os.mkdir("website")
	os.chdir("website")

	file = open("index.html", "w")
	file2 = open("style.css", "w")

	file2.write('''
body {
	background: white
}
	''')

	file.write('''
<html>
<head>
	<title>Document</title>
</head>
<body>
	<h1>
		Edit This Text In Your Text Editor.
	</h1>
</body>
</html>
	''')

main()