from flask import Flask

app = Flask(__name__)	# name 이름을 통한 flask 객체 생성

@app.route("/")				# 라우팅을 위한 뷰 함수 등록
def hello():
	return "Hi I'm LeeEunsu "

if __name__ == "__main__":	# 터미널에서 직접 실행시키면 실행 파일이 main으로 바뀜
	app.run(host="0.0.0.0", port="10111", debug=True)		# 실행을 위한 명령문으로 보면 됨. 'debug=True' 작업한 내용이 서버에  바로 반영