<template>
	<view class="">
		<view class="cu-bar bg-white margin-top solid-bottom">
			<view class="action">
				<text class="cuIcon-title text-orange"></text> 新增账号
			</view>
		</view>
		<!-- 	<scroll-view scroll-x class="bg-white nav text-center">
			<view class="cu-item" :class="index==TabCur?'text-blue cur':''" 
			v-for="(item,index) in funclist" :key="index" @tap="tabSelect" :data-id="index">
				{{item}}
			</view>
		</scroll-view> -->
		<!-- 新增品牌 -->
		<view>
			<view class="cu-form-group">
				<view class="title">姓名</view>
				<input v-model="name" class="inputbox" type="text" placeholder="请输入姓名" placeholder-class="placeclass"
					focus="true" />
				<!-- 	<input placeholder="请输入姓名" name="input" v-model="name"></input> -->
			</view>
			<view class="cu-form-group">
				<view class="title">账号</view>
				<input v-model="account" class="inputbox" type="text" placeholder="请输入账号" placeholder-class="placeclass"
					focus="true" />
				<!-- <input placeholder="请输入账号" name="input" v-model="accout"></input> -->
			</view>
			<view class="cu-form-group">
				<view class="title">密码</view>
				<input v-model="psw" class="inputbox" type="text" placeholder="请输入账号" placeholder-class="placeclass"
					focus="true" />
				<!-- <input placeholder="请输入密码" name="input" v-model="psw"></input> -->
			</view>
			<view class="cu-form-group margin-top">
				<view class="title">小组分派</view>
				<picker @change="PickerChange" :value="index" :range="picker">
					<view class="picker">
						{{index>-1?picker[index]:'请选择小组'}}
					</view>
				</picker>
			</view>
			<view class="box">
				<view class="cu-bar btn-group">
					<button class="cu-btn bg-green shadow-blur round lg" @click="create()">新增</button>
				</view>

			</view>
		</view>

	</view>
	</view>
</template>
<script>
	export default {
		onShow() {
			wx.cloud.callFunction({
				name: 'getData',
				data: {
					databaseName: 'group',
					order: 'name',
				}
			}).then(res => {
				console.log('管理员列表请求成功', res)
				console.log("res is" + res.data)
				let temp = res.result.data;
				let templist = []
				for (let item of temp) {
					templist.push(item.name)
				}
				this.picker = templist
			}).catch(err => {
				console.log('管理员列表请求失败', err)
			})
		},
		data() {
			return {
				groupchoose: "",
				picker: [],
				funclist: [
					"新增账号", "账号查看"
				],
				TabCur: 0,
				scrollLeft: 0,
				index: -1,
				newIDlist: [],
				name: "",
				account: "",
				psw: "",

				modalName: null,
				textareaAValue: '',
				textareaBValue: ''
			};
		},
		methods: {
			create() {

				if (this.name != "" && this.account != "" && this.index != -1 && this.psw != "") {
					wx.cloud.callFunction({
							name: 'addData',
							data: {
								databaseName: 'admin',
								name: this.name,
								account: parseInt(this.account),
								psw: parseInt(this.psw),
								group: this.groupchoose
							}
						})
						.then(res => {
							console.log('管理员列表请求成功', res)
							uni.navigateTo({
								url: 'admin'
							})
						})
						.catch(err => {
							console.log('管理员列表请求失败', err)
						})
				} else {
					uni.showToast({
						title: "请填写完整！"
					})
				}
			},
			PickerChange(e) {
				this.index = e.detail.value
				this.groupchoose = this.picker[this.index]
				// console.log(this.groupchoose)
			},

			CheckboxChange(e) {
				var items = this.checkbox,
					values = e.detail.value;
				for (var i = 0, lenI = items.length; i < lenI; ++i) {
					items[i].checked = false;
					for (var j = 0, lenJ = values.length; j < lenJ; ++j) {
						if (items[i].value == values[j]) {
							items[i].checked = true;
							break
						}
					}
				}
			},
			ChooseImage() {
				uni.chooseImage({
					count: 4, //默认9
					sizeType: ['original', 'compressed'], //可以指定是原图还是压缩图，默认二者都有
					sourceType: ['album'], //从相册选择
					success: (res) => {
						if (this.imgList.length != 0) {
							this.imgList = this.imgList.concat(res.tempFilePaths)
						} else {
							this.imgList = res.tempFilePaths
						}
					}
				});
			},
			ViewImage(e) {
				uni.previewImage({
					urls: this.imgList,
					current: e.currentTarget.dataset.url
				});
			},

			tabSelect(e) {
				this.TabCur = e.currentTarget.dataset.id;
				this.scrollLeft = (e.currentTarget.dataset.id - 1) * 60
				console.log(this.TabCur)
			},
			textareaAInput(e) {
				this.textareaAValue = e.detail.value
			},
		}
	}
</script>

<style>
</style>
