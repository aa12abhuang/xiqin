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
				<input placeholder="请输入姓名" name="input" v-model="name"></input>
			</view>
			<view class="cu-form-group">
				<view class="title">账号</view>
				<input placeholder="请输入账号" name="input" v-model="account"></input>
			</view>
			<view class="cu-form-group">
				<view class="title">密码</view>
				<input placeholder="请输入密码" name="input" v-model="psw"></input>
			</view>

			<view class="box">
				<view class="cu-bar btn-group">
					<button class="cu-btn bg-green shadow-blur round lg" @click="Add">新增</button>
				</view>

			</view>
		</view>

	</view>
	</view>
</template>
<script>
	export default {
		data() {
			return {
				funclist: [
					"新增账号", "账号查看"
				],
				TabCur: 0,
				scrollLeft: 0,
				index: -1,
				name: '',
				account: 0,
				psw: 0,


				modalName: null,
				textareaAValue: '',
				textareaBValue: ''
			};
		},
		methods: {
			Add() {
				wx.cloud.callFunction({
						name: 'addData',
						data: {
							databaseName: 'admin',
							name: this.name,
							account: parseInt(this.account),
							psw: parseInt(this.psw)
						}
					})
					.then(res => {
						console.log("新建成功", res)
						uni.navigateTo({
							url: './admin',
						})
					})
					.catch(err => {
						console.log("新建失败", err)
					})
			},

			PickerChange(e) {
				this.index = e.detail.value
			},
			MultiChange(e) {
				this.multiIndex = e.detail.value
			},

			TimeChange(e) {
				this.time = e.detail.value
			},
			DateChange(e) {
				this.date = e.detail.value
			},
			RegionChange(e) {
				this.region = e.detail.value
			},
			SwitchA(e) {
				this.switchA = e.detail.value
			},
			SwitchB(e) {
				this.switchB = e.detail.value
			},
			SwitchC(e) {
				this.switchC = e.detail.value
			},
			SwitchD(e) {
				this.switchD = e.detail.value
			},
			RadioChange(e) {
				this.radio = e.detail.value
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
