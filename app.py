from flask import Flask
from flask import render_template, request, send_file
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium import webdriver
import  time

app = Flask(__name__)

#@app.route('/')
#def index() :
#    return render_template('index.html')
@app.route('/')
def getInfo() :
    return render_template('index.html')

@app.route('/result',methods = ['POST','GET'])
def result():
    if request.method == 'POST':
        #print(id)
        userid = request.form['id']
        userpw =request.form['pw']
        from selenium import webdriver
        import time
        # C:\IEDriverServer.exe
        driver = webdriver.Ie('/IEDriverServer.exe')
        driver.implicitly_wait(5)
        driver.get('https://acm.sungshin.ac.kr/proweb/index1280.jsp')
        driver.find_element_by_xpath('//*[@id="saveId"]').click()
        driver.find_element_by_name('userId').send_keys(userid)
        driver.find_element_by_name('passwd').send_keys(userpw)
        driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr/td[3]/table/tbody/tr[2]/td[5]/img').click()
        driver.switch_to_frame('leftFrame')
        driver.find_element_by_xpath('//*[@id="parent2_3"]').click()
        driver.find_element_by_xpath('//*[@id="subMenu21"]').click()
        time.sleep(10)
        driver.save_screenshot("score.png")
        return send_file('score.png', mimetype= 'image/png')
        #return render_template('index.html', id = id)

if __name__ == '__main__':
    app.debug = True
    app.run()

