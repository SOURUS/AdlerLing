import _ from 'lodash';
import jsonPlaceholder from '../apis/jsonPlcaHolder';

export const fetchPosts = () =>{

    return async (dispatch) => {
        debugger;
        const response = await jsonPlaceholder.get('/posts');
        
        dispatch({ type: 'FETCH_POSTS', payload: response.data });
    };
};

export const fetchUser = (id) => {
    return async (dispatch) => {
        const response = await jsonPlaceholder.get(`/users/${id}`);

        dispatch({ type: 'FETCH_USER', payload: response.data })
    };
};

export const postsAndUsers = () => async (dispatch, getState) => {

    await fetchPosts();
    
    const userIds = _.uniq(_.map(getState().posts, 'userId'));

    userIds.forEach(id => dispatch(fetchUser(id)));
};
/*
export const fetchUser = (id) => {
    return  (dispatch) => {
        _fetchUser(id, dispatch);
    };
};

const _fetchUser = _.memoize(async (id, dispatch) => {
    const response = await jsonPlaceholder.get(`/users/${id}`);

    dispatch({ type: 'FETCH_USER', payload: response.data })
});
*/