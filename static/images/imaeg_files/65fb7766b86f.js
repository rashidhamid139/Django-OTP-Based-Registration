__d(function(g,r,i,a,m,e,d){"use strict";Object.defineProperty(e,'__esModule',{value:!0});const t={copy:r(d[0]).default,delete:r(d[1]).default,directShare:r(d[2]).default,embed:r(d[3]).default,options:r(d[4]).default,report:r(d[5]).default,share:r(d[6]).default,unfollow:r(d[7]).default};var o=r(d[9]).withRouter(function({location:o,onClose:l,openModal:u,postId:n}){const f=t[u];return a(d[8]).createElement(f,{location:o,onClose:l,postId:n})});e.default=o},19398656,[19398657,19398658,19398659,19398660,19398661,19398662,19398663,19398664,3,6]);
__d(function(g,r,i,a,m,e,d){"use strict";Object.defineProperty(e,'__esModule',{value:!0}),e.default=function({postId:t,onClose:o}){const n=r(d[0]).usePost(t,r(d[1]).getCopyUrl);return a(d[2]).createElement(i(d[3]),{onClose:o,postUrl:n})}},19398657,[16777227,16777228,3,16777223]);
__d(function(g,r,i,a,m,e,d){"use strict";Object.defineProperty(e,'__esModule',{value:!0});const t=r(d[0])(3301);e.default=function({location:o,onClose:l,postId:n}){const s=r(d[1]).useDispatch(),c=r(d[1]).useSelector(t=>r(d[2]).getViewer(t));return a(d[9]).createElement(r(d[10]).Dialog,{body:r(d[0])(3161),title:t},a(d[9]).createElement(r(d[10]).DialogItem,{color:"ig-error-or-destructive",onClick:()=>{let t;if(null!=o&&r(d[3]).isDesktop()&&i(d[4])._("160","1")){var u;o.pathname!==r(d[5]).FEED_PATH&&(t=o.pathname),(null===(u=t)||void 0===u?void 0:u.startsWith('/p/'))&&(t=r(d[6]).buildUserLink(i(d[7])(null===c||void 0===c?void 0:c.username)))}s(r(d[8]).deletePost(n,t)),l()}},r(d[11]).DELETE_TEXT),a(d[9]).createElement(r(d[10]).DialogItem,{onClick:l},r(d[11]).CANCEL_TEXT))},e.DELETE_POST_PROMPT=t},19398658,[9961476,5,9961504,9961484,9961499,10223873,9961497,9961479,10223807,3,9961500,9961491]);
__d(function(g,r,i,a,m,e,d){"use strict";Object.defineProperty(e,'__esModule',{value:!0}),e.default=function({onClose:t,postId:n}){const o=r(d[0]).useDispatch(),s=i(d[1])(),l=r(d[2]).usePost(n,r(d[3]).getPostType);r(d[4]).useEffect(()=>{r(d[5]).startFunnel(),r(d[5]).logFunnelAction(r(d[5]).SHARE_FUNNEL_BUTTON_CLICK),r(d[6]).logAction_DEPRECATED('shareClick',{source:s,type:l}),r(d[5]).logFunnelAction(r(d[5]).SHARE_FUNNEL_SHARE_SHEET),o(r(d[7]).loadPostShareIds(n))},[s,o,n,l]);const c=()=>{r(d[5]).endFunnel(),t()};return r(d[10]).getMqttInstance()&&r(d[11]).hasDirect()&&null!=n&&n.length>0&&a(d[4]).createElement(r(d[12]).Modal,{fixedHeight:!0,onClose:c,size:"large"},a(d[4]).createElement(i(d[13]),{backAction:c,forwardAction:t=>{c();const l=s;i(d[8]).logDirectEvent("DirectShareSheet",'share_sheet_send',{referral:l}),o(r(d[9]).sendPostToUsers(String(n),t))},forwardText:r(d[14]).SEND_BUTTON_STRING,includeGroup:!0,isModal:!0,pageId:"DirectShareSheet",title:r(d[14]).SHARE_TITLE}))}},19398659,[5,10223909,16777227,16777229,3,15007753,10223667,10223807,10223861,10223776,15007745,10223775,9961500,10223860,10223769]);
__d(function(g,r,i,a,m,e,d){"use strict";Object.defineProperty(e,'__esModule',{value:!0});var s=function({onClose:s,postId:o}){const t=i(d[0])(),n=r(d[1]).usePost(o,s=>s.code)||'',u=r(d[1]).usePost(o,r(d[2]).isClipsPost),l=r(d[1]).usePost(o,r(d[2]).isIGTVPost),P=r(d[1]).usePost(o,s=>!!s.isVideo),c=r(d[1]).usePost(o,s=>{var o;return i(d[3])(null===(o=s.owner)||void 0===o?void 0:o.id)});return a(d[4]).createElement(i(d[5]),{analyticsContext:t,code:n,id:o,isClipsPost:u,isGuide:!1,isIGTVPost:l,isVideo:P,onClose:s,ownerId:c})};e.default=s},19398660,[10223909,16777227,10223633,9961479,3,16777224]);
__d(function(g,r,i,a,m,e,d){"use strict";Object.defineProperty(e,'__esModule',{value:!0}),e.default=function({postId:t,onClose:o}){return a(d[0]).createElement(r(d[1]).Dialog,{onModalClose:o},a(d[0]).createElement(i(d[2]),{onClose:o,postId:t}),a(d[0]).createElement(i(d[3]),{onClose:o,postId:t}),a(d[0]).createElement(i(d[4]),{onClose:o,postId:t}),a(d[0]).createElement(i(d[5]),{onClose:o,postId:t}),a(d[0]).createElement(i(d[6]),{onClose:o,postId:t}),a(d[0]).createElement(i(d[7]),{onClose:o,postId:t}),a(d[0]).createElement(i(d[8]),{onClose:o,postId:t}),a(d[0]).createElement(r(d[1]).DialogItem,{onClick:o},r(d[9]).CANCEL_TEXT))}},19398661,[3,9961500,19398665,19398666,19398667,19398668,19398669,16777226,19398670,9961491]);
__d(function(g,r,i,a,m,e,d){"use strict";Object.defineProperty(e,'__esModule',{value:!0}),e.default=function({onClose:t,postId:o}){const s=r(d[0]).usePost(o,r(d[1]).getPostOwnedByViewer),l=r(d[0]).usePost(o,r(d[2]).getPostType),u=i(d[3])(),c=r(d[0]).usePost(o,r(d[4]).isIGTVPost),n=r(d[5]).useSetPostModal();let P=r(d[6]).isMobile()||c;return r(d[6]).isDesktop()&&!0===i(d[7])._("160","1")&&(P=!0),s&&P?a(d[9]).createElement(r(d[10]).DialogItem,{color:"ig-error-or-destructive",onClick:()=>{r(d[8]).logAction_DEPRECATED('delete_post_click',{source:u,type:l}),n('delete')}},r(d[11])(2323)):null}},19398665,[16777227,19398671,16777229,10223909,10223633,13500433,9961484,9961499,10223667,3,9961500,9961476]);
__d(function(g,r,i,a,m,e,d){"use strict";Object.defineProperty(e,'__esModule',{value:!0}),e.getPostOwnedByViewer=function(t){var n;return(null===(n=t.owner)||void 0===n?void 0:n.id)===r(d[0]).getViewerId()}},19398671,[9961487]);
__d(function(g,r,i,a,m,e,d){"use strict";Object.defineProperty(e,'__esModule',{value:!0});const o=r(d[0])(417);e.default=function({onClose:t,postId:n}){const s=r(d[1]).usePost(n,r(d[2]).getPostOwnedByViewer),c=r(d[3]).useSetPostModal();return s?null:a(d[7]).createElement(r(d[8]).DialogItem,{color:"ig-error-or-destructive",onClick:()=>{r(d[4]).isUserLoggedIn()?c('report'):r(d[5]).redirect(r(d[6]).buildLoginLink(window.location.href,{source:'logged_out_post_report_redirect'}))}},o)}},19398666,[9961476,16777227,19398671,13500433,10223706,9961477,9961497,3,9961500]);
__d(function(g,r,i,a,m,e,d){"use strict";function o(o,t){const n=r(d[1]).getPostById(o,t),{owner:l}=n;if(!l)return!1;const u=r(d[2]).getRelationship(o.relationships,l.id);return r(d[2]).followedByViewer(u)}Object.defineProperty(e,'__esModule',{value:!0});const t=r(d[0])(1746);e.default=function({postId:n,onClose:l}){const u=r(d[3]).useSelector(t=>o(t,n)),s=r(d[4]).useSetPostModal(),c=r(d[5]).usePost(n,o=>{var t;return null===(t=o.owner)||void 0===t?void 0:t.id}),f=i(d[6])();return u?a(d[8]).createElement(r(d[9]).DialogItem,{color:"ig-error-or-destructive",onClick:()=>{r(d[7]).logConnectionAction({eventName:'unfollow_button_tapped',containerModule:f,targetId:c}),s('unfollow')}},t):null}},19398667,[9961476,10223802,10223624,5,13500433,16777227,10223909,10223753,3,9961500]);
__d(function(g,r,i,a,m,e,d){"use strict";Object.defineProperty(e,'__esModule',{value:!0}),e.default=function({onClose:t,postId:o}){const n=r(d[0]).useSelector(r(d[1]).selectPageIdentifier),l=r(d[2]).usePost(o,t=>{var o;return!!(null===(o=t.code)||void 0===o?void 0:o.length)})&&n!==i(d[3]).postPage,s=r(d[2]).usePost(o,r(d[4]).getShareURL);return l?a(d[6]).createElement(r(d[7]).DialogItem,{onClick:()=>{i(d[5]).push(s)}},r(d[8])(815)):null}},19398668,[5,10223745,16777227,9961489,16777228,9961477,3,9961500,9961476]);
__d(function(g,r,i,a,m,e,d){"use strict";Object.defineProperty(e,'__esModule',{value:!0}),e.default=function({onClose:t,postId:n}){const o=r(d[0]).usePostAndOwner(n,r(d[1]).getIsShareable),s=r(d[2]).useSetPostModal();return o?a(d[3]).createElement(r(d[4]).DialogItem,{onClick:()=>s('share')},r(d[5])(988)):null}},19398669,[16777227,16777228,13500433,3,9961500,9961476]);
__d(function(g,r,i,a,m,e,d){"use strict";Object.defineProperty(e,'__esModule',{value:!0});const t=r(d[0])(2963),o=r(d[0])(2554);e.default=function({onClose:s,postId:n}){const c=r(d[1]).usePostAndOwner(n,r(d[2]).getIsShareable),u=r(d[3]).useSetPostModal(),l=i(d[4])(),p=i(d[5])(),P=r(d[1]).usePost(n,r(d[6]).getPostType),y=r(d[1]).usePost(n,r(d[2]).getCopyUrl);return c?a(d[9]).createElement(r(d[10]).DialogItem,{onClick:()=>{if(!r(d[7]).canCopy())return void u('copy');const o=r(d[7]).copy(y);r(d[8]).logAction_DEPRECATED('postLinkCopy',{source:p,type:P}),o?(l({text:t}),s()):u('copy')}},o):null},e.LINK_COPIED_PROMPT=t,e.COPY_LINK_TEXT=o},16777226,[9961476,16777227,16777228,13500433,12976138,10223909,16777229,16646272,10223667,3,9961500]);
__d(function(g,r,i,a,m,e,d){"use strict";Object.defineProperty(e,'__esModule',{value:!0}),e.default=function({postId:o,onClose:t}){const n=r(d[0]).usePostAndOwner(o,r(d[1]).getIsShareable),s=r(d[2]).useSetPostModal(),l=i(d[3])(),u=r(d[0]).usePost(o,r(d[4]).getPostType),c=r(d[0]).usePost(o,o=>{var t;return null===(t=o.owner)||void 0===t?void 0:t.id});return n?a(d[6]).createElement(r(d[7]).DialogItem,{onClick:()=>{r(d[5]).logAction_DEPRECATED('embedCodeClick',{mediaId:o,ownerId:c,source:l,type:u}),s('embed')}},r(d[8])(846)):null}},19398670,[16777227,16777228,13500433,10223909,16777229,10223667,3,9961500,9961476]);
__d(function(g,r,i,a,m,e,d){"use strict";Object.defineProperty(e,'__esModule',{value:!0}),e.default=function({onClose:n,postId:o}){const t=r(d[0]).usePostAndOwner(o,(n,o)=>o.id),s=r(d[0]).usePostAndOwner(o,(n,o)=>o.username),u=r(d[0]).usePostAndOwner(o,(n,o)=>o.profilePictureUrl),l=i(d[1])();return a(d[2]).createElement(i(d[3]),{analyticsContext:l,onClose:n,ownerID:t,ownerProfilePicURL:u,ownerUsername:s,postID:o})}},19398662,[16777227,10223909,3,19398672]);
__d(function(g,r,i,a,m,e,d){"use strict";Object.defineProperty(e,'__esModule',{value:!0}),e.default=function({postId:t,onClose:n}){const s=r(d[0]).useDispatch(),o=i(d[1])(),u=r(d[2]).usePost(t,r(d[3]).getPostType),l=r(d[2]).usePost(t,t=>{var n;const s=(null===(n=t.owner)||void 0===n?void 0:n.username)||'';return r(d[4]).getShareDescription(s,u)}),c=r(d[2]).usePostAndOwner(t,r(d[5]).getIsShareable),_=r(d[2]).usePost(t,t=>t.shareIds),E=r(d[2]).usePost(t,r(d[5]).getShareURL);return r(d[6]).useEffect(()=>{r(d[7]).startFunnel(),r(d[7]).logFunnelAction(r(d[7]).SHARE_FUNNEL_BUTTON_CLICK),r(d[8]).logAction_DEPRECATED('shareClick',{source:o,type:u}),r(d[7]).logFunnelAction(r(d[7]).SHARE_FUNNEL_SHARE_SHEET),s(r(d[9]).loadPostShareIds(t))},[o,s,t,u]),a(d[6]).createElement(i(d[10]),{analyticsContext:o,description:l,onClose:()=>{r(d[7]).endFunnel(),n()},onNativeShare:()=>{r(d[8]).logAction_DEPRECATED('nativeShareClick',{source:o,type:u}),r(d[7]).logFunnelAction(r(d[7]).SHARE_FUNNEL_NATIVE),n(),r(d[4]).shareWithNative(l,E,'ig_web_button_native_share').then(r(d[7]).endFunnel)},postId:t,postType:u,shareEnabled:c,shareIds:_,url:E,utmSource:"ig_web_button_share_sheet"})}},19398663,[5,10223909,16777227,16777229,15007752,16777228,3,15007753,10223667,10223807,15007756]);
__d(function(g,r,i,a,m,e,d){"use strict";Object.defineProperty(e,'__esModule',{value:!0}),e.default=function({postId:t,onClose:n}){const o=i(d[0])(),s=r(d[1]).usePost(t,t=>{var n;return null===(n=t.owner)||void 0===n?void 0:n.id});return a(d[2]).createElement(i(d[3]),{analyticsContext:o,analyticsExtra:{},onClose:n,userId:s})}},19398664,[10223909,16777227,3,16253037]);