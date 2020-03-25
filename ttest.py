#t-test
def ttest(data):

    control_a = data[data["group"]==0]["gmv"]
    control_b = data[data["group"]==1]["gmv"]
    N1 = len(control_a)
    N2 = len(control_b)
    var1 = control_a.var()
    var2 = control_b.var()
    dof = (N1 + N2 - 2)
    std_N1N2 = np.sqrt(((N1 - 1)*var1 + (N2 - 1)*var2) / dof)
    MoE = t.ppf(0.95, dof) * std_N1N2 * np.sqrt(1/N1 + 1/N2)
    diff_mean = control_a.mean()-control_b.mean()
    print('treatment_mean {:3.2f}'.format(control_a.mean()))
    print('control_mean {:3.2f}'.format(control_b.mean()))
    print('Absolute difference is {:3.2f} [{:3.2f}, {:3.2f}] (mean [95% CI])'.format(diff_mean, diff_mean - MoE, diff_mean + MoE))
    print('Relative difference is {:3.2f}%'.format(diff_mean/control_b.mean()*100))
    print(ttest_ind(control_a,control_b)) 

dongguan = aa_data[aa_data["city_id"]==36]
dongguan["group"] = dongguan.apply(divide_group, axis=1)
ttest(dongguan)

#p-value
control_a = dongguan[dongguan["group"]==0]["is_finish"]
control_b = dongguan[dongguan["group"]==1]["is_finish"]
N1 = len(control_a)
N2 = len(control_b)
std1 = control_a.std()
std2 = control_b.std()
dof = (N1 + N2 - 2)
p1 = control_a.mean()
p2 = control_b.mean()
tstats = (p2-p1)/np.sqrt(p1*(1-p1)/N1+p2*(1-p2)/N2)
dof = N1+N2-2
p = 2*(t.sf(abs(tstats), dof))
p