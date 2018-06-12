/**
 * OBWOptions - filter controller
 * version: 0.0.1
 * author: jfw
 * date: 2017.12.04
 * 
 * @param id string:tab的id，全域唯一，不可重复。
 * @param options JSON:页面的条件选择控件配置信息。
 * @param timeType JSON:时间粒度，默认激活日维度(current:"date")
 * @param YYCR JSON:同环比，默认没有初始化(current=0),页面统一按照以下格式
 * <div class="checkbox  js-noTag $id$-yy">
 *    <input class="$id$-yy" type="radio" name="$id$-yycr" value="1">
 *    <i></i>
 *</div>
 *<span class="text $id$-yy-span">同比</span>
 *<div class="checkbox  js-noTag $id$-cr">
 *    <input class="$id$-cr" type="radio" name="$id$-yycr" value="2">
 *    <i></i>
 *</div>
 *<span class="text $id$-cr-span">环比</span>
 */
function OBWOptions(id,options,timeType,YYCR) {
    this.options = $.extend({parent:this},options);
    this.timeType = $.extend({active:"date",current:"date"},timeType);
    this.YYCR = $.extend({init:false,current:0},YYCR);
    this.id = id;
}

/**
 * 初始化所有控件的入口方法。
 */
OBWOptions.prototype.initOptions = function () {
	this.initTimeType();
	this.initYYCR();
	
    for ( var option in this.options) {
        if(typeof(this.options[option]) ==="object" && this.options[option]['init']){
            this.options[option].parent=this.options;
            var data = this.options[option]["data"];
            var url = this.options[option]["url"];
            
            if(typeof(data) === "object"){//默认初始化值或者已经初始化过了。
                var func = this.options[option]['init'];
                if(!func){
                    return;
                }
                this[func].call(this.options[option]);
            }else if (typeof(url) === "string" && url.length > 0) {//对象且有URL
                $jsonData =$.extend(this.options[option].param,{
                        $id$ : option
                }) ;
                this.sendAjax( this.options,$jsonData,url);
            }
        }
    }
};

/**
 * 初始化时间粒度控件及事件 日周月年日期控件及周期控件联动选择
 */
OBWOptions.prototype.initTimeType = function () {
	if(!$.isEmptyObject(this.timeType)){
		var buildDateStrategy = DataPick.buildDateStrategy('#'+this.id);
		buildDateStrategy[this.timeType.active]();
		$('#'+this.id+' .timeUnit-box').on('change', 'input[type=radio]',_this=this, function () {
				buildDateStrategy[$(this).val()]();
				_this.timeType["current"] = $(this).val();
				if(_this.YYCR.init){
					if($(this).val()=="year"){
						$("."+_this.id+"-cr:radio").removeAttr("checked");
						$("div."+_this.id+"-cr,."+_this.id+"-cr-span").hide(); 
						$("."+_this.id+"-yy:radio").attr("checked","true");
						_this.YYCR["current"]=$("."+_this.id+"-yy:radio").val();; 
					}else {
						$("div."+_this.id+"-cr,."+_this.id+"-cr-span").show(); 
					}
				}
		});
	}
}

/**
 * 初始化同环比控件事件
 */
OBWOptions.prototype.initYYCR = function () {
	if(this.YYCR.init){
		$("input[name='"+this.id+"-yycr']").off('click').on('click',_this=this,function(){
		    	var val = $("input[name='"+_this.id+"-yycr']:checked").val();
		    	val = typeof(val) == "undefined" ? 0 : val;	
		    	if(val==_this.YYCR["current"]){
		    		$("input[name='"+_this.id+"-yycr']").removeAttr("checked");
		    		_this.YYCR["current"]=0;
		    	} else {
		    		_this.YYCR["current"]=val;
		    	}
		});
	}
}

/**
 * 发送ajax请求,返回数据存到$obj对应的控件属性的data上，然后初始化控件的init方法。
 * @param $obj 请求的OBWOptions.options对象
 * @param $jsonData 请求的参数
 * @param url 请求的url
 */
OBWOptions.prototype.sendAjax = function ($obj,$jsonData,url) {
    $.ajax({
			type : "post",
			url : "/operationboard/rest/report/fetcher/openess/" + url,
			data : JSON.stringify($jsonData),
			dataType : "json",
			success : function(response) {
				var $data = JSON.parse(this.data);
				var qResult = JSON.parse(response.Result.Data);
				if($obj[$data.$id$] && !$obj[$data.$id$].data){
					$obj[$data.$id$].data={};
				}
				$obj[$data.$id$].data=qResult;
				var func = $obj[$data.$id$]['init'];
				if(!func){
					return;
				}
				$obj.parent[func].call($obj[$data.$id$]);
				$obj.parent.setfilterHead();
			},
			error : function() {
				alert("获取数据失败！");
			}
		});
};

/**
 * 单下拉框
 * this 指向options下的控件属性
 * @param param
 */
OBWOptions.prototype.selectRenderingInit = function (param) {
    var _this=this;
    var _options = this.parent;
    var _obwOptions = _options.parent;
	var entry = this.entry;
	if(!this.data){
		return;
	}
	var parents = this.data[entry.parentId];
	var values = this.data[entry.value];
	var names = this.data[entry.name];
	
	var html="";
	_this.current = [];//当前选中的值和文本
	if(this.hasAll){
		if(this.allValue){
			_this.current[0] = this.allValue;
			html+='<li name="'+this.allValue+'" class="current"><span>全部</span></li>';
		}else{
			_this.current[0] = ".*";
			html+='<li name=".*" class="current"><span>全部</span></li>';
		}

		_this.current[1] = "全部";
	}
	
	if(!param){
		var initOptionUL = _obwOptions.heredoc(function(){/*
			<div class="filter-detail-wrap" id="$id$">
			    <div class="filter-detail-item filter-detail-item-1 show">
			        <div class="filter-detail-content">
			            <ul class="filter-detail-list" from="$id$"  id="$listId$">

			            </ul>
			        </div>
			    </div>
			</div>*/});

		initOptionUL = initOptionUL.replace(/\$id\$/g,this.filterId);
		initOptionUL = initOptionUL.replace(/\$listId\$/g,this.optionId);
		$("#"+_obwOptions.id).append(initOptionUL);
	}
	
	for(var i=0;i<values.length;i++){
		if(param && parents && -1 == param.indexOf(parents[i])){
			continue;
		}
		if(html.length == 0){
			_this.current[0] = values[i];
			_this.current[1] = names[i];
			html +='<li name="'+values[i]+'" class="current"><span>'+names[i]+'</span></li>';
		}else {
			html +='<li name="'+values[i]+'"><span>'+names[i]+'</span></li>';
		}
	}
	$('#'+this.optionId).html("");
	$('#'+this.optionId).append(html);
	var controller = $('#'+_obwOptions.id+'Filter').find('[data-filter-detail='+this.filterId+']');
	controller.siblings('span').text(_this.current[1]);
	
	//初始化依赖控制function
	if(_this.depend){
		var func = _obwOptions[_this.depend[0]];
		if(typeof(func) === "function"){
			func(_this);
		}
	}
	//bind click event
	$('#'+this.optionId).find("li").off('click').on('click',_this,function () {
		var $this = $(this);
		$this.addClass('current');
		$this.siblings().removeClass('current');
		var selectedText = $this.find("span").text();// 选择的option
		var selectedValue = $this.attr("name");// 选择的option
		var $thisFilterButtom = $('#'+_obwOptions.id).find('[data-filter-detail='+_this.filterId+']');
		$thisFilterButtom.siblings('span').text(selectedText);
		_this.current = [];//当前选中的值和文本
		_this.current[0]=selectedValue;
		_this.current[1]=selectedText;
		$('#'+_this.filterId).removeClass("show");//隐藏下拉框
		
		//如果有级联则初始化联动控件。
		if(!$.isEmptyObject(_this.casecade)){
			for ( var i in _this.casecade) {
				var func =_options[_this.casecade[i]]['init'];
                if(!func){
                    return;
                }
                _obwOptions[func].call(_options[_this.casecade[i]],_this.current);
			}
		}
		
		//自定义事件回调方法
		if(_this.depend && _this.depend[1]){
			var func = _obwOptions[_this.depend[1]];
			if(typeof(func) === "function"){
				func(_this);
			}
		}

		_obwOptions.setfilterHead();
	});
};
/**
 * 多下拉框 TODO
 * @param param
 */
OBWOptions.prototype.multiSelectRenderingInit = function (param) {};
/**
 * 单/复选框
 * @param param
 */
OBWOptions.prototype.checkBoxRenderingInit = function (param) {
    var _this=this;
    var _options = this.parent;
    var _obwOptions = _options.parent;
	var entry = this.entry;
	if(!this.data){
		return;
	}
	var parents = this.data[entry.parentId];
	var values = this.data[entry.value];
	var names = this.data[entry.name];
	
	$('#'+this.optionId).empty();
	var html='<div class="checkbox  js-noTag ">'+
                    '<input type="checkbox"  value=".*" class="'+this.filterId+'_checkall" checked>'+
                    '<i></i>'+
                '</div>'+
				'<span class="text">全部</span>';

	_this.current = [[],[]];//当前选中的值和文本
	
	for(var i=0;i<values.length;i++){
		if(param && parents && -1 == param.indexOf(parents[i])){
			continue;
		}
		_this.current[0].push(values[i]);
		_this.current[1].push(names[i]);
		html +='<div class="checkbox"><input type="checkbox" value="'+values[i]+'" class="'+this.filterId+'" checked>'
		+'<i></i></div><span class="text data_center">'+names[i]+'</span>'
	}
	$('#'+this.optionId).append(html);
	
	//bind check box change event
	$('#'+this.optionId+' .checkbox').off('change').on('change',_this,function () {
		if($(this).find("input").attr("value") == ".*"){//全部的选择事件可以忽略
			return false;
		}
		//变更当前选中的值和名称
		var checkedValue = $(this).find("input").attr("value");
		var checkedName = $(this).next("span").text();
		var index = _this.current[0].indexOf(checkedValue);
		if( index == -1){
			_this.current[0].push(checkedValue);
			_this.current[1].push(checkedName);
		}else{
			_this.current[0].splice(index,1);
			_this.current[1].splice(index,1);
		}
		
		//自定义事件回调方法
		if(_this.depend && _this.depend[0]){
			var func = _obwOptions[_this.depend[0]];
			if(typeof(func) === "function"){
				func(_this);
			}
		}
		
		_obwOptions.setfilterHead();
	});
	
	$('#'+this.optionId).checkall({
    	checkall: '.'+this.filterId+'_checkall',
    	checkbox: '.'+this.filterId+':not(:disabled)'
	});
}

/**
 * 多行字符串处理。
 * @param fn
 */
OBWOptions.prototype.heredoc= function (fn)  {
    return fn.toString().split('\n').slice(1,-1).join('\n') + '\n';
}

/**
 * 由对象实例实现的方法,设置头部信息。
 */
OBWOptions.prototype.setfilterHead= function ()  {}
