from apps import create_cms_app

# 传入配置文件信息
cms_app = create_cms_app('apps.settings.DevConfig')

if __name__ == '__main__':
    # 创建数据库
    with cms_app.app_context():
        from apps.models import db

        db.create_all()
    # 运行程序
    cms_app.run()
