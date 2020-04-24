const Todos = require('../model/todoModels')

exports.test = (request, response) => {
    response.send('ini udah bener komunikasi antar model dan routes')

}
exports.create = (request, response) => {
    let todos = new Todos({   //Todos dari nama event exportnya
        name: request.body.name,
        activity: request.body.activity,
        done: false  //default
    })
    todos.save((error, res) => {
        if (error) {
            response.json({ message: "failed input" })
        } else {
            response.json({ message: "input successed" })
        }

    })
}

exports.todoShow = (request, response) => {
    Todos.find({}, (error, result) => {
        if (error) {
            response.json({ message: "failed" })
        } else {
            response.json(result)
        }
    })
}
exports.todoDetails = (request, response) => {
    let id = request.params.id

    Todos.findById(id, (error, result) => { //menacri berdasarkan id
        if (error) {
            response.json({ message: "failed" })
        } else {
            response.json(result)
        }
    })
}

exports.todoUpdate = (request, response) => {
    let id = request.params.id

    Todos.findByIdAndUpdate(id, { $set: request.body }, (error, result) => { //mencari berdasarkan id
        if (error) {                                                            //request.body -> mengupdate request yang ada di body
            response.json({ message: "failed" })
        } else {
            response.json(result)
        }
    })
}
exports.todoDelete = (request, response) => {
    let id = request.params.id

    Todos.findByIdAndRemove(id, (error, result) => { //mencari berdasarkan id
        if (error) {                                                            //request.body -> mengupdate request yang ada di body
            response.json({ message: "failed" })
        } else {
            response.json(result)
        }
    })
}