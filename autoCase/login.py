from playwright.sync_api import sync_playwright


def login_to_lingxing(url, username, password):
    with sync_playwright() as p:
        # 启动无头浏览器,显示浏览器界面
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # 导航到登录页面
        page.goto(url)

        print("页面标题:", page.title())

        # 等待用户名和密码输入框加载完成
        page.wait_for_selector("input[name='account']")
        page.wait_for_selector("input[type='password']")

        # 输入用户名和密码
        page.fill("input[name='account']", username)
        page.fill("input[type='password']", password)

        # 点击登录按钮
        page.click("button[type='button']")

        # 等待登录后的页面加载完成
        page.wait_for_load_state("networkidle")

        # 验证登录是否成功（可选）
        # 例如，检查某个特定的元素是否存在
        if page.query_selector(".logo.mp-el-menu"):
            print("登录成功！")
            cookies = context.cookies()
            token = None
            for cookie in cookies:
                # 示例：匹配键名为 'token' 或 'access_token' 的 Cookie
                if cookie["name"] in ["token", "auth-token"]:
                    token = cookie["value"]
                    print(f"成功获取 Cookie Token：{token}")
                    break
        else:
            print("登录失败！")



        # 关闭浏览器
        # browser.close()


def get_token(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        # 等待页面加载完成
        page.wait_for_load_state("networkidle")
        # 从 LocalStorage 获取 Token
        token = page.evaluate("localStorage.getItem('token')")
        print(f"Token: {token}")
        browser.close()


login_to_lingxing('https://erp.lingxing.com/login','wuwang','afs123456')
