// 更新值入口文件
const cloud = require('wx-server-sdk')

cloud.init()

// 更新值云函数入口函数
exports.main = async (event, context) => {

	cloud.database().collection(event.databaseName)
		.where({
			name: event.name
		})
		.update({
			data: {
				name: event.name,
				account: parseInt(event.account),
				psw: parseInt(event.psw)
			}
		})
}
