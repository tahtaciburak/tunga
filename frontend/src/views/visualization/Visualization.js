import React, { useEffect, useState, createRef } from 'react'
import {
	CCol, CBadge,
	CCard,
	CCardBody,
	CCardHeader,
	CDataTable,
	CButton,
	CRow,
	CSelect,
	CInputCheckbox,
	CLabel,
	CFormGroup
} from '@coreui/react'
import {
	CChartBar,
	CChartLine,
	CChartDoughnut,
	CChartRadar,
	CChartPie,
	CChartPolarArea
} from '@coreui/react-chartjs'
//import usersData from '../users/UsersData'
import APIService from '../../services/APIService'
import AlertService from '../../services/AlertService'

import translate from '../../services/i18n/Translate';

class Visualization extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			datasets: [],
			columns: [],
			selectedDatasetId: -1,
			selectedColumnId: -1,
			isShowResult: false,
			steps: [
				"lowercase",
				"uppercase",
				"remove_stopwords",
				"remove_digits",
				"remove_emails",
				"remove_urls",
				"remove_emojis",
				"remove_hashtags",
				"remove_mentions",
				"remove_non_turkish_words",
				"correct_typos",
				"lemmatize",
				"stem",
				"asciify",
				"deasciify"
			],
			selectedSteps: {
				lowercase: false,
				uppercase: false,
				remove_stopwords: false,
				remove_digits: false,
				remove_emails: false,
				remove_urls: false,
				remove_emojis: false,
				remove_hashtags: false,
				remove_mentions: false,
				remove_non_turkish_words: false,
				correct_typos: false,
				lemmatize: false,
				stem: false,
				asciify: false,
				deasciify: false
			}
		}
		this.handleDatasetNameChange = this.handleDatasetNameChange.bind(this);
		this.handleColumnChange = this.handleColumnChange.bind(this);
		this.handleCheckboxClick = this.handleCheckboxClick.bind(this);
	}

	componentDidMount() {
		this.fetchDatasets();
	}

	handleDatasetNameChange(event) {
		let datasetId = event.target.value;
		this.setState({ selectedDatasetId: datasetId });
		this.fetchColumns(datasetId);
	}

	handleColumnChange(event) {
		let columndId = event.target.value;
		this.setState({ selectedColumnId: columndId });
	}

	handleCheckboxClick(event) {
		let cname = event.target.name;
		let isChecked = event.target.checked;
		let actualSelected = this.state.selectedSteps;
		actualSelected[cname] = isChecked;
		this.setState({ selectedSteps: actualSelected });
	}

	handleSubmitButtonClick(event) {
		alert("datayi sunucuya gonder")
	}

	async fetchDatasets() {
		await APIService.requests
			.get('dataset/all')
			.then(data => {
				console.log(data.datasets)
				this.setState({ datasets: data.datasets })
			})
			.catch(data => {
				console.log(data)
				AlertService.Add({
					type: 'alert',
					//message: translate.getText('error.' + data.response.body.error.code),
					level: 'error',
					autoDismiss: 5
				});
			});
	}

	async fetchColumns(datasetId) {
		await APIService.requests
			.get('dataset/' + datasetId + '/columns')
			.then(data => {
				console.log(data.columns)
				this.setState({ columns: data.columns })

			})
			.catch(data => {
				this.setState({ columns: [] })
				console.log(data)
				AlertService.Add({
					type: 'alert',
					//message: translate.getText('error.' + data.response.body.error.code),
					level: 'error',
					autoDismiss: 5
				});
			});
	}


	render() {
		return (
			<>
				<div className="card">
					<div className="card-header">
						{translate.translate("visualization.header")}
					</div>
					<div className="card-body">
						<CCol xs="12" lg="12">
							<CCard>
								<CCardHeader>
									{translate.translate("visualization.choose_dataset")}
								</CCardHeader>
								<CCardBody>
									<CFormGroup row>
										<CCol md="3">
											<CLabel htmlFor="select">{translate.translate("machine_learning.topic_modelling.dataset")}</CLabel>
										</CCol>
										<CCol xs="12" md="9">
											<CSelect onChange={this.handleDatasetNameChange} custom name="select" id="select">
												<option value="0">{translate.translate("machine_learning.topic_modelling.please_choose")}</option>

												{this.state.datasets.map((ds, i) =>
													<option key={i} value={i}>{ds.filename}</option>

												)}
											</CSelect>
										</CCol>
									</CFormGroup>

								</CCardBody>
							</CCard>
							<CRow>
								<CCol>
									<CCard>
										<CCardHeader>
											Pie Chart
        </CCardHeader>
										<CCardBody>
											<CChartPie
												type="pie"
												datasets={[
													{
														backgroundColor: [
															'#41B883',
															'#E46651',
															'#00D8FF',
															'#DD1B16'
														],
														data: [40, 20, 80, 10]
													}
												]}
												labels={['VueJs', 'EmberJs', 'ReactJs', 'AngularJs']}
												options={{
													tooltips: {
														enabled: true
													}
												}}
											/>
										</CCardBody>
									</CCard>
								</CCol>
								<CCol>
									<CCard>
										<CCardHeader>
											Bar Chart
          <div className="card-header-actions">
												<a href="http://www.chartjs.org" className="card-header-action">
													<small className="text-muted">docs</small>
												</a>
											</div>
										</CCardHeader>
										<CCardBody>
											<CChartBar
												type="bar"
												datasets={[
													{
														label: 'GitHub Commits',
														backgroundColor: '#f87979',
														data: [40, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 11]
													}
												]}
												labels="months"
												options={{
													tooltips: {
														enabled: true
													}
												}}
											/>
										</CCardBody>
									</CCard>
								</CCol>
							</CRow>
							<CRow>
								<CCol>
									<CCard>
										<CCardHeader>
											Radar Chart
        </CCardHeader>
										<CCardBody>
											<CChartRadar
												type="radar"
												datasets={[
													{
														label: '2019',
														backgroundColor: 'rgba(179,181,198,0.2)',
														borderColor: 'rgba(179,181,198,1)',
														pointBackgroundColor: 'rgba(179,181,198,1)',
														pointBorderColor: '#fff',
														pointHoverBackgroundColor: '#fff',
														pointHoverBorderColor: 'rgba(179,181,198,1)',
														tooltipLabelColor: 'rgba(179,181,198,1)',
														data: [65, 59, 90, 81, 56, 55, 40]
													},
													{
														label: '2020',
														backgroundColor: 'rgba(255,99,132,0.2)',
														borderColor: 'rgba(255,99,132,1)',
														pointBackgroundColor: 'rgba(255,99,132,1)',
														pointBorderColor: '#fff',
														pointHoverBackgroundColor: '#fff',
														pointHoverBorderColor: 'rgba(255,99,132,1)',
														tooltipLabelColor: 'rgba(255,99,132,1)',
														data: [28, 48, 40, 19, 96, 27, 100]
													}
												]}
												options={{
													aspectRatio: 2,
													tooltips: {
														enabled: true
													}
												}}
												labels={[
													'Eating', 'Drinking', 'Sleeping', 'Designing',
													'Coding', 'Cycling', 'Running'
												]}
											/>
										</CCardBody>
									</CCard>

								</CCol>
								<CCol>

									<CCard>
										<CCardHeader>
											Line Chart
        </CCardHeader>
										<CCardBody>
											<CChartLine
												type="line"
												datasets={[
													{
														label: 'Data One',
														backgroundColor: 'rgb(228,102,81,0.9)',
														data: [30, 39, 10, 50, 30, 70, 35]
													},
													{
														label: 'Data Two',
														backgroundColor: 'rgb(0,216,255,0.9)',
														data: [39, 80, 40, 35, 40, 20, 45]
													}
												]}
												options={{
													tooltips: {
														enabled: true
													}
												}}
												labels="months"
											/>
										</CCardBody>
									</CCard>
								</CCol>
							</CRow>
							<CRow>
								<CCol>
								<CCard>
									<CCardHeader>
												Word Cloud
									</CCardHeader>
									<CCardBody>
												sdfsdfad
									</CCardBody>
								</CCard>

								</CCol>
							</CRow>
						</CCol>
					</div>
				</div>
			</>
		)
	}
}

export default Visualization

/**
 *
 *
 *

 */