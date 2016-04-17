/**
 * Created by liveangel on 15-8-4.
 * 兼容IE10,和Windows Phone 8 Update 3 (a.k.a. GDR3) 版本之前的设备
 */

// Copyright 2014-2015 Twitter, Inc.
// Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
if (navigator.userAgent.match(/IEMobile\/10\.0/)) {
    var msViewportStyle = document.createElement('style')
    msViewportStyle.appendChild(
        document.createTextNode(
            '@-ms-viewport{width:auto!important}'
        )
    )
    document.querySelector('head').appendChild(msViewportStyle)
}
