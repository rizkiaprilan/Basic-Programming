const express = require('express')
const router = express.Router()

const todoController = require('../controller/todoController')  //ambil controllernya

router.get('/test',todoController.test)
router.post('/create',todoController.create)
router.get('/',todoController.todoShow)
router.get('/:id',todoController.todoDetails)
router.put('/:id/update',todoController.todoUpdate)
router.delete('/:id/delete',todoController.todoDelete)



module.exports = router
