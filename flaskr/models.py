from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from flaskr.extensions import db
from flaskr.utils import constants


class User(db.Model, UserMixin):
    """用户信息表"""
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    hash_password = db.Column(db.String(512), unique=False, nullable=False)
    name = db.Column(db.String(20), unique=False, nullable=False)
    birthday = db.Column(db.Date)
    sex = db.Column(db.String(16))
    # 是否有效，无效用户将不能登录系统
    status = db.Column(db.Integer, default=constants.UserStatus.USER_ACTIVE.value)
    # 是否是超级管理员，管理员可以对所有内容进行管理
    is_super = db.Column(db.Integer, default=constants.UserRole.COMMON.value)
    # 创建时间
    created_at = db.Column(db.DateTime, default=datetime.now)
    user_profile = db.relationship('UserProfile', backref='profile', uselist=False)

    @property
    def password(self):
        raise AttributeError('password cannot be read')

    @password.setter
    def password(self, password):
        self.hash_password = generate_password_hash(password)

    def confirm_password(self, password):
        return check_password_hash(self.hash_password, password)

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return f'<{self.id}, {self.name}, {self.sex}, {self.birthday}>'

    # 最后修改的时间

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        """ 有效的用户才能登录系统 """
        return self.status == constants.UserStatus.USER_ACTIVE.value

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return '{}'.format(self.id)

    @property
    def cuber_333_best(self):
        return self.cuber_333.filter(AchievementCuber333.best.isnot(None)).order_by(AchievementCuber333.best).first()

    @property
    def cuber_333_ao5(self):
        return self.cuber_333.filter(AchievementCuber333.ao5.isnot(None)).order_by(AchievementCuber333.ao5).first()

    @property
    def cuber_222_best(self):
        return self.cuber_222.filter(AchievementCuber222.best.isnot(None)).order_by(AchievementCuber222.best).first()

    @property
    def cuber_222_ao5(self):
        return self.cuber_222.filter(AchievementCuber222.best.isnot(None)).order_by(AchievementCuber222.best).first()

    @property
    def cuber_oh_best(self):
        return self.cuber_oh.filter(AchievementCuberOh.best.isnot(None)).order_by(AchievementCuberOh.best).first()

    @property
    def cuber_oh_ao5(self):
        return self.cuber_oh.filter(AchievementCuberOh.best.isnot(None)).order_by(AchievementCuberOh.best).first()

    @property
    def cuber_py_best(self):
        return self.cuber_py.filter(AchievementCuberPy.best.isnot(None)).order_by(AchievementCuberPy.best).first()

    @property
    def cuber_py_ao5(self):
        return self.cuber_py.filter(AchievementCuberPy.best.isnot(None)).order_by(AchievementCuberPy.best).first()

    @property
    def cuber_sk_best(self):
        return self.cuber_sk.filter(AchievementCuberSk.best.isnot(None)).order_by(AchievementCuberSk.best).first()

    @property
    def cuber_sk_ao5(self):
        return self.cuber_sk.filter(AchievementCuberSk.best.isnot(None)).order_by(AchievementCuberSk.best).first()

    @property
    def get_user_avatar(self):
        return self.user_profile

    @property
    def get_user_confidentiality(self):
        return self.user_confidentiality.first()

    @property
    def cuber_333_all(self):
        results = db.session.query(CompetitionInformation.match_name,
                                   CompetitionInformation.id,
                                   AchievementCuber333).join(Info).join(AchievementCuber333).filter(
            self.id == AchievementCuber333.user_id).order_by(CompetitionInformation.match_time.desc()).all()
        return results

    @property
    def cuber_222_all(self):
        results = db.session.query(CompetitionInformation.match_name,
                                   CompetitionInformation.id,
                                   AchievementCuber222).join(Info).join(AchievementCuber222).filter(
            self.id == AchievementCuber222.user_id).order_by(CompetitionInformation.match_time.desc()).all()
        return results

    @property
    def cuber_oh_all(self):
        results = db.session.query(CompetitionInformation.match_name,
                                   CompetitionInformation.id,
                                   AchievementCuberOh).join(Info).join(AchievementCuberOh).filter(
            self.id == AchievementCuberOh.user_id).order_by(CompetitionInformation.match_time.desc()).all()
        return results

    @property
    def cuber_py_all(self):
        results = db.session.query(CompetitionInformation.match_name,
                                   CompetitionInformation.id,
                                   AchievementCuberPy).join(Info).join(AchievementCuberPy).filter(
            self.id == AchievementCuberPy.user_id).order_by(CompetitionInformation.match_time.desc()).all()
        return results

    @property
    def cuber_sk_all(self):
        results = db.session.query(CompetitionInformation.match_name,
                                   CompetitionInformation.id,
                                   AchievementCuberSk).join(Info).join(AchievementCuberSk).filter(
            self.id == AchievementCuberSk.user_id).order_by(CompetitionInformation.match_time.desc()).all()
        return results

    # @property
    # def get_competition_all(self):
    #     results = db.session.query(CompetitionInformation.match_name, CompetitionInformation.id).join(Info)\
    #
    #     return result


class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    avatar = db.Column(db.String(256))


class UserLoginHistory(db.Model):
    __tablename__ = 'user_login_history'
    id = db.Column(db.Integer, primary_key=True)  # 主键
    # 用户名，用于登录
    username = db.Column(db.String(64), nullable=False)
    # IP地址
    ip = db.Column(db.String(32))
    # user-agent
    ua = db.Column(db.String(512))
    # 创建时间
    created_at = db.Column(db.DateTime, default=datetime.now)
    # 关联用户
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # 建立与用户的一对多属性,user.history_list
    user = db.relationship('User', backref=db.backref('history_list', lazy='dynamic'))


class UserConfidentiality(db.Model):
    __tablename__ = 'user_confidentiality'
    id = db.Column(db.Integer, primary_key=True)
    confidentiality_question = db.Column(db.Text)
    confidentiality_answer = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('user_confidentiality', lazy='dynamic'))


class Info(db.Model):
    """
    参赛选手信息信息
    """
    __tablename__ = 'player_information'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(5), unique=False, nullable=False)
    mobile = db.Column(db.String(11), unique=False, nullable=False)
    birthday = db.Column(db.Date, unique=False, nullable=False)
    registration_items = db.Column(db.String(50), unique=False, nullable=False)
    # 外键关联比赛表
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    match_id = db.Column(db.Integer, db.ForeignKey('competition_information.id'))
    match = db.relationship('CompetitionInformation', backref=db.backref('competition'))
    user = db.relationship('User', backref=db.backref('user_player_info', lazy='dynamic'))
    add_time = db.Column(db.DateTime, default=datetime.now)


class CompetitionInformation(db.Model):
    """
    比赛信息详情表
    """
    __tablename__ = 'competition_information'
    id = db.Column(db.Integer, primary_key=True)
    # 比赛时间
    match_time = db.Column(db.Date, unique=False, nullable=False)
    # 比赛地址
    address = db.Column(db.String(150), unique=False, nullable=False)
    # 报名人数上限
    number_of_applicants = db.Column(db.String(4), nullable=False)
    # 开设项目
    project_opening = db.Column(db.String(500), nullable=False)
    # 比赛的名字
    match_name = db.Column(db.String(200), nullable=False)
    # 基础报名费
    registration_fee = db.Column(db.String(4), nullable=True)
    # 项目报名费
    item_registration_free = db.Column(db.String(4), nullable=True)
    # 报名截止时间
    registration_end_time = db.Column(db.Date, nullable=False)
    # 比赛详情
    details = db.Column(db.Text)
    enter_status = db.Column(db.Integer, default=constants.MatchEnter.FUTURE_ENTER.value)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('match'))

    def __unicode__(self):
        return self.match_name

    def __repr__(self):
        return f'<{self.id}, {self.match_name}, {self.match_time}>'


class Banner(db.Model):
    """轮播图"""
    __tablename__ = 'home_banner'
    id = db.Column(db.Integer, primary_key=True)
    image_route = db.Column(db.Text)
    add_time = db.Column(db.Date, default=datetime.now)
    index = db.Column(db.Integer)
    match_id = db.Column(db.ForeignKey('competition_information.id'))


class OderInfo(db.Model):
    """用户报名缴费订单表"""
    __tablename__ = 'oder_info'
    id = db.Column(db.Integer, primary_key=True)
    # 订单号
    oder_id = db.Column(db.Integer)
    add_time = db.Column(db.DateTime, unique=True)
    # 金额
    amount = db.Column(db.String(10))
    match_id = db.Column(db.Integer, db.ForeignKey('competition_information.id'))
    user = db.relationship('User', backref=db.backref('user_oder_info', lazy='dynamic'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Achievement(db.Model):
    __tablename__ = 'achievement_table'
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('competition_information.id'))
    address = db.Column(db.String(150), unique=False, nullable=False)
    match_name = db.Column(db.String(200), nullable=False)
    match_time = db.Column(db.Date, unique=False, nullable=False)


class AchievementCuber333(db.Model):
    __tablename__ = 'achievement_cuber_333'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('cuber_333', lazy='dynamic'))
    match_id = db.Column(db.Integer, db.ForeignKey('competition_information.id'))
    match = db.relationship('CompetitionInformation', backref=db.backref('match_cuber_333', lazy='dynamic'))
    t1 = db.Column(db.Float)
    t2 = db.Column(db.Float)
    t3 = db.Column(db.Float)
    t4 = db.Column(db.Float)
    t5 = db.Column(db.Float)
    best = db.Column(db.Float)
    ao5 = db.Column(db.Float)
    competition_options = db.Column(db.String(10))


class AchievementCuber222(db.Model):
    __tablename__ = 'achievement_cuber_222'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('cuber_222', lazy='dynamic'))
    match_id = db.Column(db.Integer, db.ForeignKey('competition_information.id'))
    match = db.relationship('CompetitionInformation', backref=db.backref('match_cuber_222', lazy='dynamic'))
    t1 = db.Column(db.Float)
    t2 = db.Column(db.Float)
    t3 = db.Column(db.Float)
    t4 = db.Column(db.Float)
    t5 = db.Column(db.Float)
    best = db.Column(db.Float)
    ao5 = db.Column(db.Float)
    competition_options = db.Column(db.String(10))


class AchievementCuberPy(db.Model):
    __tablename__ = 'achievement_cuber_py'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('cuber_py', lazy='dynamic'))
    match_id = db.Column(db.Integer, db.ForeignKey('competition_information.id'))
    match = db.relationship('CompetitionInformation', backref=db.backref('match_cuber_py', lazy='dynamic'))
    t1 = db.Column(db.Float)
    t2 = db.Column(db.Float)
    t3 = db.Column(db.Float)
    t4 = db.Column(db.Float)
    t5 = db.Column(db.Float)
    best = db.Column(db.Float)
    ao5 = db.Column(db.Float)
    competition_options = db.Column(db.String(10))


class AchievementCuberSk(db.Model):
    __tablename__ = 'achievement_cuber_sk'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('cuber_sk', lazy='dynamic'))
    match_id = db.Column(db.Integer, db.ForeignKey('competition_information.id'))
    match = db.relationship('CompetitionInformation', backref=db.backref('match_cuber_sk', lazy='dynamic'))
    t1 = db.Column(db.Float)
    t2 = db.Column(db.Float)
    t3 = db.Column(db.Float)
    t4 = db.Column(db.Float)
    t5 = db.Column(db.Float)
    best = db.Column(db.Float)
    ao5 = db.Column(db.Float)
    competition_options = db.Column(db.String(10))


class AchievementCuberOh(db.Model):
    __tablename__ = 'achievement_cuber_oh'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('cuber_oh', lazy='dynamic'))
    match_id = db.Column(db.Integer, db.ForeignKey('competition_information.id'))
    match = db.relationship('CompetitionInformation', backref=db.backref('match_cuber_oh', lazy='dynamic'))
    t1 = db.Column(db.Float)
    t2 = db.Column(db.Float)
    t3 = db.Column(db.Float)
    t4 = db.Column(db.Float)
    t5 = db.Column(db.Float)
    best = db.Column(db.Float)
    ao5 = db.Column(db.Float)
    competition_options = db.Column(db.String(10))


class IndexArticle(db.Model):
    __tablename__ = 'index_article'
    id = db.Column(db.Integer, primary_key=True)
    release_time = db.Column(db.Date, nullable=False)
    title = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('article'))
    content = db.Column(db.Text, nullable=False)
