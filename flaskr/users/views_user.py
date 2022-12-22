import os
from flask import redirect, flash, render_template, url_for, request
from flask_login import logout_user, login_required, current_user

from config import Config
from flaskr.models import User, UserProfile, UserConfidentiality, CompetitionInformation, Info
from flaskr.users import users
from flaskr.users.forms import LoginForms, RegisterForm, UserEditForm, ForgetPasswordFrom
from flaskr.extensions import db


@users.route('/logout')
def logout():
    logout_user()  # 登出用户
    return redirect(url_for('match.index'))


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForms()
    next_url = request.values.get('next', url_for('match.index'))
    # 后台admin登录
    if form.validate_on_submit():
        user = form.do_login()
        if user:
            if next_url:
                return redirect(next_url)
            else:
                return flash('登录失败，请稍后重试', 'danger')
    return render_template('users/login.html', form=form, next_url=next_url)


@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        form.do_register()
        flash('注册成功', 'success')
        return redirect(url_for('users.login'))
    return render_template('users/register.html', form=form)


@users.route('/webpage/user_id=<int:user_id>')
@login_required
def webpage(user_id):
    user = User.query.get(user_id)
    user_avatar = user.get_user_avatar
    user_ach = {
        'cuber_333_best': user.cuber_333_best,
        'cuber_333_ao5': user.cuber_333_ao5,
        'cuber_222_best': user.cuber_222_best,
        'cuber_222_ao5': user.cuber_222_ao5,
        'cuber_oh_best': user.cuber_oh_best,
        'cuber_oh_ao5': user.cuber_oh_ao5,
        'cuber_py_best': user.cuber_py_best,
        'cuber_py_ao5': user.cuber_py_ao5,
        'cuber_sk_best': user.cuber_sk_best,
        'cuber_sk_ao5': user.cuber_sk_ao5,
    }
    user_competition_count = Info.query.filter_by(user_id=user_id).count()
    return render_template('users/webpage.html',
                           user=user, user_ach=user_ach,
                           user_avatar=user_avatar,
                           user_competition_count=user_competition_count)


@users.route('/my_information', methods=['GET', 'POST'])
@login_required
def my_information():
    if request.args:
        filename = request.args.get('filename')
        if current_user.user_profile:
            # file_ = current_user.user_profile.avatar
            # try:
            #     os.remove(Config.UPLOADED_PATH + "photo/" + file_)
            # except FileNotFoundError as e:
            #     pass
            db.session.query(UserProfile).filter(UserProfile.user_id == current_user.id).update(
                {'avatar': filename}
            )
        else:
            user_obj = UserProfile(avatar=filename, user_id=current_user.id)
            db.session.add(user_obj)
        db.session.commit()
    if current_user.user_profile:
        avatar = current_user.get_user_avatar.avatar
        return render_template('users/my_information.html', avatar=avatar)
    return render_template('users/my_information.html', avatar=None)


@users.route('/my_registration')
@login_required
def my_registration():
    registration = db.session.query(Info, CompetitionInformation).join(
       Info, Info.match_id == CompetitionInformation.id
    ).filter(Info.user_id == current_user.id).all()
    return render_template('users/my_registration.html', registration=registration)


@users.route('forget_password', methods=['GET', 'POST'])
def forget_password():
    form = ForgetPasswordFrom()
    if form.validate_on_submit():
        user = db.session.query(User).filter_by(id=current_user.id).first()
        user.password = form.confirm_password.data
        db.session.commit()
        flash('密码修改成功', 'success')
    return render_template('users/forget_password.html', form=form)


@users.route('user_edit', methods=['GET', 'POST'])
@login_required
def user_edit():
    form = UserEditForm()
    if form.validate_on_submit():
        db.session.query(User).filter_by(id=current_user.id).update(
            {
                'name': form.name.data,
                'sex': form.sex.data,
                'birthday': form.birthday.data,
            }
        )
        db.session.query(UserConfidentiality).filter_by(user_id=current_user.id).update(
            {
                'confidentiality_question': form.confidentiality_question.data,
                'confidentiality_answer': form.confidentiality_answer.data
            }
        )
        db.session.commit()
        flash('提交成功', 'success')
    return render_template('users/user_edit.html', form=form)
