from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory 'database'
students = []
next_id = 1


@app.route('/')
def index():
	return render_template('list.html', students=students)


@app.route('/create', methods=['GET', 'POST'])
def create():
	global next_id
	if request.method == 'POST':
		name = request.form.get('name', '').strip()
		age = request.form.get('age', '').strip()
		if name:
			students.append({'id': next_id, 'name': name, 'age': age})
			next_id += 1
		return redirect(url_for('index'))
	return render_template('form.html', action=url_for('create'))


@app.route('/edit/<int:sid>', methods=['GET', 'POST'])
def edit(sid):
	student = next((s for s in students if s['id'] == sid), None)
	if not student:
		return redirect(url_for('index'))
	if request.method == 'POST':
		name = request.form.get('name', '').strip()
		age = request.form.get('age', '').strip()
		if name:
			student['name'] = name
			student['age'] = age
		return redirect(url_for('index'))
	return render_template('form.html', action=url_for('edit', sid=sid), student=student)


@app.route('/delete/<int:sid>', methods=['POST'])
def delete(sid):
	global students
	students = [s for s in students if s['id'] != sid]
	return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(debug=True)

