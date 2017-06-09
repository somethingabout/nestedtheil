def tnest(data, c1, i, c2):
    theil = Th(data, c1, i, c2)
    theil = pd.merge(theil.rename(columns= {'sum c1w':'sum c1c2w'}), theil.groupby([c1]).sum()[['sum c1w']].reset_index(), on = [c1])
    theil['wshare'] = theil['sum c1c2w']/theil['sum c1w']
    theil['wi'] =(theil['wshare']*theil['t'])
    wi = theil[['wi',c1]].groupby(c1).sum().reset_index()
    theil = pd.merge(theil, data[[c1, i, c2]].groupby([c1, c2]).mean().reset_index().rename(columns = {i: 'c1c2mean'}), on = [c1,c2])
    theil = pd.merge(theil, data[[c1,i]].groupby(c1).mean()[[i]].reset_index().rename(columns = {i: 'c1mean'}), on = [c1])
    theil['bw'] = theil['wshare']*(np.log(theil['c1c2mean']/theil['c1mean']))
    bw = theil[['bw', c1]].groupby(c1).sum().reset_index()
    tnest = pd.merge(bw,wi, on = c1)
    
    theil = theil[[c1,'c1mean']]
    wbar = theil['c1mean'].mean()
    theil['s']= theil['c1mean']/wbar
    theil['slns'] = theil['s']*np.log(theil['s'])
    t  = (1/ntot)*theil['slns'].sum()
    
    return tnest t

    '''
    This creates a nested within Theil, between Theil for any subset.
    Th() function is required to run tnest().
    
    Parameters
    ----------
    data: dataframe
    c1: group (ie occupation)
    c2: group (industry), optional
    i: variable (ie income)
        '''